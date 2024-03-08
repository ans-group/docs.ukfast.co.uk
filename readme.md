# Welcome to the ANS Documentation Repository

All the documentation is published on <https://www.ans.co.uk/docs/>

If you would like to contribute a guide or amendment to an existing one, please fork the repository and submit a pull request.

To get started, please visit:

* [the "how to contribute" guide](https://github.com/ans-group/docs.ukfast.co.uk/blob/master/contribute.md)
* [the terminology and style guide](https://github.com/ans-group/docs.ukfast.co.uk/blob/master/guide.md)

## Developing locally

There are a number of ways you can develop locally.

You _can_ also use the `docker-compose.dev.yml` Docker Compose file, which will build a full environment, including Elasticsearch and populating it. For making small changes, however, you might find this tedious as you will need to rebuild the containers on every change.

Generally, the easiest way is to run `sphinx-autobuild`, which will give you a live preview of the ANS Docs site using your local data. This automatically rebuilds any changed docs content.

This does have some drawbacks. Firstly, only content in the `/source` directory is auto-rebuilt, so no theme CSS or JavaScript. They are rendered at at the start, but changes are not detected. Secondly, there is no search functionality possible.

### Using a Docker container

One of the easiest ways is to use a Linux server with Docker installed. Using the command below will start up a container, map in the current directory and set up port forwarding for `8000/tcp`, as defined in `docker-compose.devlocal.yml`.

```bash
docker-compose -f docker-compose.devlocal.yml up -d
```

Once the container has started up fully (which can take a few minutes), you should be able to browse to `http://127.0.0.1:8000` and see content. If you want to access the content remotely, replace `127.0.0.1` with the correct IP of your Linux server.

If you need to see the build logs, you can do so with:

```bash
docker logs sphinx_autobuild
```

### Using Python

You can install all the dependencies to run Sphinx using the commands in the `Autobuild-Dockerfile` file. Generally, however, you will need to have these packages installed:

* Package Manager | `make`, Python 3.6+
* PIP | `sphinx-autobuild`, `recommonmark`

Once those are in place, you should be able to start `sphinx-autobuild` like this:

```bash
sphinx-autobuild \
   --pre-build "make build/html/_static/css/app.css" \
   --pre-build "make build/html/_static/app.js" \
   --host 0.0.0.0 \
   source build/html
```

### Testing your content

There are a few commands you can use to check the content is correct:

#### Check for broken links

This will go through the content and make sure there are no broken links within the content.

```console
make linkcheck
```

#### Markdown Linting

If you're using Docker for development, you can run this to check whether the content meets the linting requirements:

```bash
docker run \
   -v "$PWD:/app" \
   -w /app \
   --rm \
   markdownlint/markdownlint source
```

#### Spell checking

We are using PySpelling for this. Similarly, if you're using Docker for development, you can run this to check whether the content meets the spell check requirements:

```bash
docker run \
   -v "$PWD:/app" \
   -w /app \
   --rm \
   -e INPUT_SOURCE_FILES="source/**/*.md" \
   -e INPUT_TASK_NAME=Markdown \
   rojopolis/spellcheck-github-actions:0.10.0
```

You can change the `$INPUT_SOURCE_FILES` variable to be whatever you want. It will accept a space-separated list of files.

There are __two word lists__ in place which control the spell checking:

1. The first is `.wordlist.txt` which has all of the words we use in ANS and the IT field in it. You should add more words to this, but only if they are legitimate and correct in terms of upper and lower case.
1. The second is `.wordlist-workaround.txt` which contains non-words and partial words to work around limitations in PySpelling.

   One example of this is `L2TP`. As `aspell` (which powers PySpelling) splits words first on non-word characters, `L2TP` is seen as two different words, `L` and `TP`. Similarly, word contractions like `ANS's` will we seen as invalid, as will hyphenated words.

   So, you should add these workarounds to this file, __not__ the `.wordlist.txt` file.

You can also wrap words with the HTML tag `<nospell>`, which will cause PySpelling to ignore the word.

## Page Construction and Key Elements

### Naming and Path

Please ensure pages and folders are easy to read and sensibly structured.

Please keep the page URLs lowercase and use hyphens instead of spaces, e.g.

* `/docs/desktop/fastdesk/getting-started/windows/`

### Navigation, Page Heading and Meta

When adding a new page these elements need to be considered to help site readability, usability, navigation and search results. Here's info on what each does, how to set them and some guidelines.

#### Page Heading (H1)

Sets the main heading for the page

```eval_rst
.. image:: https://user-images.githubusercontent.com/30502984/86182420-d9c66d00-bb27-11ea-929f-5b4025c6e6b1.png
   :width: 500
```

To set:

* Within `.md` files (normal content pages), add as first piece of content.

```markdown
# Transferring a Domain to ANS
```

* Within `index.rst` files (category index pages, which list the `.md` pages underneath), add to top of file.

```rst
======================
Domain Name Management
======================
```

The `h1` tag is the title of the article and should give the reader a strong sense of what they are going to read. It should be between 20 and 70 characters, but this is not enforced. There should only be one `h1`-level heading on a page, and it should be the first on the page.

#### Page Navigation and Breadcrumb

**By default** the page navigation and breadcrumb is populated from the Page Heading, and often this is perfectly fine. Sometimes, a longer page heading is better for the user, but long sentences will fill up the `nav` and push the breadcrumbs off the page. If you want a longer page title (`h1`), set the `nav` item specifically, as shown:

![image](https://user-images.githubusercontent.com/30502984/86183731-902b5180-bb2a-11ea-826b-6172fabd6236.png)

You can override the name of the page in the Table of Contents and sidebar too. Those are defined in `index.rst` files. Use the format `Page Title <filename-on-disk-minus-extension>` to achieve that, for example:

```rst
.. toctree::
   :maxdepth: 1

   Transfering to ANS <transferin>
   Transfering from ANS <transferout>
   Changing Nameservers <changingnameservers>
   DNS Propagation <dnspropagation>
```

#### Page Meta Title

This meta content determines how the page is displayed in search engine results. It's crucial for the overall performance of the website from an SEO perspective and it helps the user with history, bookmarks and the site search.

##### Appearance on Google

```eval_rst
.. image:: https://user-images.githubusercontent.com/30502984/86184852-e1d4db80-bb2c-11ea-82d7-7ac5938aa705.png
   :width: 500
```

##### Use in the browser

```eval_rst
.. image:: https://user-images.githubusercontent.com/30502984/86185226-c0282400-bb2d-11ea-9eeb-a086c17d2a45.png
   :width: 500
```

##### Use in the site search

This is how they are displayed to the user in the site search results

```eval_rst
.. image:: https://user-images.githubusercontent.com/30502984/86186022-d6cf7a80-bb2f-11ea-80c0-94ac1342e28e.png
   :width: 500
```

In many cases the meta title can be the same as the Page Heading. However, there are character length limitations we must adhere to, so they may require shortening.

Also, give the content a description as this can help search results. Of course, though, the page content is much more important.

##### For `.md` files (normal content pages)

Please note spacing and indents are important, so copy this template.

Meta content looks like this and goes at the bottom of the file:

<pre>
```eval_rst
   .. title:: Creating an eCloud Flex instance
   .. meta::
      :description: Detailed guidance on creating OpenStack instances on eCloud Flex
      :keywords: openstack, ecloud flex, ans, nova, instance, virtual machine, vm
```
</pre>

##### For `index.rst` files (category index pages, which list the `.md` pages underneath

Meta content goes at the top of the page, otherwise it will fail our automated checks

<pre>
   .. title:: Email | Email hosting
   .. meta::
      :description: Information regarding a wide range of email related issues
      :keywords: ans, email, exim, postfix, mail, dovecot, blocklist, dkim, spf
</pre>

As you'll see, the content is the same except for being wrapped in an `eval_rst` fence.

### Character length limitations for meta

- `title` - maximum of 42 characters. Don't include "| ANS Documentation" at the end as this is will be added via the template.
- `description` - maximum of 165 characters

Your pull request will fail the automated checks without this meta content in the correct format.

## Adding elements to the page content

Most content is simple Markdown (`md`), but some features require reStructuredText (`rst`). The format is quite different compared to Markdown, and needs to be inside `eval_rst` blocks. Here are a few examples of how to add more types of content.

### Images / screenshots

Where relevant, please add screenshots to pages as image files (ideally `.png`).  This is especially useful when describing how to complete a task in Myans, for instance. Please blur out any sensitive information such as account names or IP addresses, as necessary.  Most image editors will allow you to add a blurred box over the image. This looks a lot neater than using a "black marker pen" style.

Given the following structure:

```console
.
├── document.md
├── files
│   ├── image.png
```

We can include `image.png` in `document.md` using Markdown as below (with `someimage` becoming the `alt` text):

```markdown
![someimage](files/image.png)
```

Or using reStructuredText (to control height and width) as below:

<pre>
```eval_rst

.. image:: files/image.png
   :width: 400
```
</pre>

Example image, the text preceding becomes the Alt text

### Tables

```eval_rst
.. note:: Tables need to be in reStructuredText format otherwise they won't display properly when published. It _will_ look fine in Git, but will look horrible when published, trust me!
```

There are free tools that will generate RST for you, like <http://www.tablesgenerator.com/text_tables#>.

This is an example which works. Note the requirement to wrap in the `eval_rst` fence block.

<pre>
```eval_rst
===========   ========   =========================================================
Record Type   Hostname   Target
===========   ========   =========================================================
CNAME         portal     64cf9871a5b0ca045an96udtf9a63687c180f47df6.user.ddosx.com
===========   ========   =========================================================
```
</pre>


### Hyperlinks

For internal site links the easiest form to add them is like this:

* In Markdown

If you wish to use text other than the heading for the section that you're linking to, use the following format:

  * For internal links

  ```markdown
  [text to show](link-to-page)
  ```

  *  For external links

  ```markdown
  [Go to the domain transfer in page in ANS Portal](https://portal.ans.co.uk/domains/transfer-in.php).
  ```

* In reStructuredText

```rst
:doc:`/ecloud/flex/general/openstackcli`
```

This will make a hyperlink using the title of the page `/docs/ecloud/flex/general/openstackcli` as the text.

If you wish to use text other than the heading for the section that you're linking to, use the following format:

```rst
:doc:`Custom Text</ecloud/flex/general/openstackcli>`
```

You can also use this syntax:

```rst
`Custom Text</docs/ecloud/flex/general/openstackcli>`_
```

If you need to link headings (anchors) in other pages, you may need to use this format, which separates the display text away from the hyperlink target:

```rst
.. note::
   Please see our user guide on `connecting to your website via FTP`_ for further assistance.

.. _connecting to your website via FTP: /docs/operatingsystems/windows/commonissues/copyfiletoserver#connecting-to-your-ftp-server
```

You'll notice that `connecting to your website via FTP` is used as a reference to associate the two.

```eval_rst
.. warning::
     Avoid using words like 'link', 'click here' or 'here' as the linking text. These are harder to pick out for the user, and offer no idea of where the link will take them unless they read the preceeding content, which makes it harder. The text should give a good idea to the user where it will take them when reading it alone.
```

### Adding Notes, Info, Warning, etc.

These must be done using reStructuredText, and the format is like this:

<pre>
```eval_rst
.. note::

   Sectigo also provide an online EV click-through as an alternative. This is available on request.

```
</pre>

See the file in path `/domains/ssl/extended_validation_ssl` as an example.
 * [Markdown source](https://github.com/ans-group/docs.ukfast.co.uk/edit/master/source/domains/ssl/extended_validation_ssl.md)
 * [Rendered page](https://docs.ukfast.co.uk/docs/domains/ssl/extended_validation_ssl.html#)

#### Adding the Registered Trademark ®

Adding this:
<pre>
DDoSX\ :sup:`®`\
</pre>

Renders like this: DDoSX<sup>®</sup>

## Deploy Locally
Ensure you have `docker` and `docker-compose` installed.

```bash
git clone https://github.com/ans-group/docs.ukfast.co.uk.git ans_docs
cd ans_docs
docker-compose -f docker-compose.dev.yml up --build
```

Open a browser to 'http://localhost/docs'
