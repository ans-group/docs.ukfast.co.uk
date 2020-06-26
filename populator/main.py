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

directory = './'
file_type = '.md'
remove_list = [r'.. (.*?)::']
another_list = ['eval_rst', ':doc:', '`',
                '\\ :sup:', ' | UKFast Documentation']
meta_words = [':title:', ':description:', ':keywords:']

hostname = 'elasticsearch'
host = 'http://' + hostname + ':9200'


class Colour:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    LIGHT_BLUE = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


def setup_logging():
    logging.basicConfig(
        # filename='log',
        # filemode='w+',
        level=logging.INFO,
        format='%(asctime)s | %(levelname)-10s | %(name)-20s | %(filename)-20s  | %(funcName)-30s | %(lineno)-5d | %(message)s'
        # format='%(asctime)s | %(message)s'
    )

    logging.addLevelName(logging.CRITICAL, "\033[1;91;43m{}\033[0m".format(" ******** "))

    logging.addLevelName(logging.INFO, "{}{:10}{}".format(
        Colour.BLUE,
        logging.getLevelName(logging.INFO),
        Colour.ENDC)
    )

    logging.addLevelName(logging.WARNING, "{}{:10}{}".format(
        Colour.YELLOW,
        logging.getLevelName(logging.WARNING),
        Colour.ENDC)
    )

    logging.addLevelName(logging.ERROR, "{}{:10}{}".format(
        Colour.RED,
        logging.getLevelName(logging.ERROR),
        Colour.ENDC)
    )

    logging.getLogger("sqlalchemy").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)


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
        for remove in remove_list:
            plain_text = re.sub(remove, '', plain_text)
        for remove in another_list:
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
            output += line

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
        title = re.search(':title: (.*)\\b', text).group(1).strip()
        description = re.search(':description: (.*)\\b', text).group(1).strip()
        keywords = re.search(':keywords: (.*)\\b', text).group(1).split(',')
    except:
        pass

    return sanitise(title), sanitise(description), keywords


def approximate_meta(text):
    """
    Takes the fist and second non-blank lines as the title and description.
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


def format_markdown_text(text):
    """
    Input a doc.md file and it'll spit out the title, description, keywords (perhaps), and the content.
    """
    output = prettify(text)
    title, desc, keywords = get_meta(text)

    if not title or not desc:
        title, desc = approximate_meta(text)
        print('Missing proper meta tags...')

    # print('title: {}'.format(title))
    # print('desc: {}'.format(desc))
    # print('keys: {}'.format(keywords))
    # print('body: {}'.format(output))
    # print('\n')

    return {
        'title': title,
        'description': desc,
        'keywords': ' '.join(keywords),
        'content': output
    }


if __name__ == '__main__':
    setup_logging()
    logging.info('waiting for es at {}'.format(hostname))

    while True:
        if check_elasticsearch_alive(host):
            break
        time.sleep(3)

    index = 'documentation'
    es = None

    while True:
        try:
            es = Elasticsearch(host=hostname, port=9200)
            es.ping()
            break
        except:
            logging.exception('sleeping')
            time.sleep(5)

    # Create the documentation index and set the 'boost' levels for the columns.
    # Essentially lets us prioritse columns in searches.
    request_body = """
    {
        "mappings": {
            "properties": {
              "keywords": {
                "type": "text",
                "boost": 4
              },
              "title": {
                "type": "text",
                "boost": 3
              },
              "description": {
                "type": "text",
                "boost": 2
              },
              "content": {
                "type": "text",
                "boost": 1
              }
            }
        }
    }
    """

    es.indices.create(index=index, body=request_body)

    logging.info('Populating elasticsearch...')

    target = 'source'
    logging.info(list_md_files_in_dir(target))
    for file in list_md_files_in_dir(target):
        logging.info('Processing {}...'.format(file))
        output = format_markdown_text(open(file, 'r').read())
        output['url'] = '/' + file.replace(target, '').replace('.md', '.html')
        res = es.index(index=index, body=output)

    logging.info('Done!')
