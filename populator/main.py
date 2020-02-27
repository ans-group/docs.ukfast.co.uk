from markdown import markdown
import requests
import re
import html2text
from bs4 import BeautifulSoup
import os
import logging
from elasticsearch import Elasticsearch
import shutil
import sys
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)-10s | %(filename)-20s  | %(funcName)-30s | %(lineno)-5d | %(message)s')
logging.getLogger("elasticsearch").setLevel(logging.WARNING)

file_type = '.md'
remove_regex = [r'.. (.*?)::']
remove_list = ['eval_rst', ':doc:', '`', '\\ :sup:', ' | UKFast Documentation']
meta_words = [':title:', ':description:', ':keywords:']
hostname = 'elasticsearch'
host = 'http://' + hostname + ':9200'

index_name = os.getenv('ESINDEX', 'documentation')
source_dir = os.getenv('SOURCEDIR', 'source')


def check_elasticsearch_alive(host):
    try:
        url = host + '/_search?q=test'
        headers = {'content-type': 'application/json'}
        requests.post(url, headers=headers)
    except:
        return False
    return True


def sanitise(text):
    try:
        plain_text = text
        for remove in remove_regex:
            plain_text = re.sub(remove, '', plain_text)
        for remove in remove_list:
            plain_text = plain_text.replace(remove, '')
    except:
        pass
    return plain_text


def prettify(text):
    """
    Convert the markdown to html using the markdown module,
    then get Beautiful soup to convert that to plain text.
    # NoCode
    """
    plain_text = ''.join(BeautifulSoup(
        markdown(text), features="html.parser").findAll(text=True))

    # Get rid of all the weird artefacts from markdown rules we've violated.
    plain_text = sanitise(plain_text)

    output = ''
    # Also get rid of the meta lines we stick at the bottom of some files.
    for line in plain_text.split('\n'):
        safe = True
        for word in meta_words:
            if word in line:
                safe = False
                break
        if safe:
            output += line + '  \n'

    return output


def get_meta(text):
    """
    Pulls out the meta info from the files that have it:
        title
        description
        keywords
    """
    title = None
    description = None
    keywords = []

    try:
        title = re.search(':title: (.*)\\b', text).group(1)
        description = re.search(':description: (.*)\\b', text).group(1)
        keywords = re.search(':keywords: (.*)\\b', text).group(1).split(',')
    except:
        pass

    return sanitise(title), sanitise(description), keywords


def approximate_meta(text):
    """
    Takes the first and second non-blank lines as the title and description.
    Only called on files that don't have the meta info at the bottom.
    """
    lines = text.split('\n')
    title = None
    description = None

    for line in lines:
        if len(line) > 2:
            if not title:
                title = ''.join(ch for ch in line if ch.isalnum() or ch == ' ')
                continue
            if not description and line.startswith('#') is False and line.startswith('..') is False and line.startswith(
                    '``') is False:
                description = line
                break

    return sanitise(title), sanitise(description)


def list_md_files_in_dir(dir_):
    """
    Useful if you've cloned the docs repo.
    """
    file_paths = []
    try:
        for root, _, files in os.walk(dir_):
            for file in files:
                if file.endswith(file_type):
                    file_paths.append(os.path.join(root, file))
    except:
        logging.exception('')
    return file_paths


def format_markdown_text(text, file):
    """
    Input a doc.md file and it'll spit out the title, description, keywords (perhaps), and the content.
    """
    output = prettify(text)
    title, desc, keywords = get_meta(text)

    if not title or not desc:
        title, desc = approximate_meta(text)
        logging.warning('Missing proper meta tags in {}'.format(file))
    else:
        logging.info('Found meta data for {}'.format(file))

    return {
        'title': title,
        'description': desc,
        'keywords': ' '.join(keywords),
        'content': output
    }


if __name__ == '__main__':
    logging.info('Waiting for the elasticsearch to become responsive at {}...'.format(hostname))

    while True:
        if check_elasticsearch_alive(host):
            break
        time.sleep(3)

    es = None

    while True:
        try:
            es = Elasticsearch(host=hostname, port=9200)
            es.ping()
            break
        except:
            logging.exception('sleeping')
            time.sleep(5)

    if es.indices.exists(index=index_name):
        logging.warning('Elasticsearch index \'{}\' already exists. Attempting to delete...'.format(index_name))
        es.indices.delete(index=index_name, ignore=[400, 404])

    # Create the documentation index and set the 'boost' levels for the columns.
    # Essentially lets us prioritse columns in searches.
    # Could do with converting this to python.
    request_body = """
    {
        "mappings": {
            "properties": {
              "title": {
                "type": "text",
                "boost": 10
              },
              "keywords": {
                "type": "text",
                "boost": 5
              },
              "description": {
                "type": "text",
                "boost": 3
              },
              "content": {
                "type": "text",
                "boost": 1
              }
            }
        }
    }
    """

    es.indices.create(index=index_name, body=request_body)

    logging.info('Populating elasticsearch...')

    logging.info(list_md_files_in_dir(source_dir))
    missing_meta = 0
    found_meta = 0
    for file in list_md_files_in_dir(source_dir):

        logging.info('Processing {}...'.format(file))

        output = format_markdown_text(open(file, 'r').read(), file)
        if output['keywords'] == '':
            missing_meta += 1
        else:
            found_meta += 1

        output['url'] = file.replace(source_dir, '').replace('.md', '.html')
        es.index(index=index_name, body=output)

    logging.info('Total documents missing meta tags {}/{}'.format(missing_meta, missing_meta + found_meta))
    logging.info('Done!')
