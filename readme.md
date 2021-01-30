# Welcome to the UKFast Documentation Repository

All the documentation is published on <https://docs.ukfast.co.uk/>

If you would like to contribute a guide or amendment to an existing one, please fork the repository and submit a pull request.

To get started, please visit:

* [the "how to contribute" guide](https://github.com/ukfast/docs.ukfast.co.uk/blob/master/contribute.md)
* [the terminology and style guide](https://github.com/ukfast/docs.ukfast.co.uk/blob/master/guide.md)

## Page Construction and Key Elements

### Naming and Path

Please ensure pages and folders are easy to read and sensibly structured.

Please keep the page URLs lowercase and use hyphens instead of spaces, e.g.

* `/desktop/fastdesk/getting-started/windows.html`

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
# Transferring a Domain to UKFast
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

   Transfering to UKFast <transferin>
   Transfering from UKFast <transferout>
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
      :keywords: openstack, ecloud flex, ukfast, nova, instance, virtual machine, vm
```
</pre>

##### For `index.rst` files (category index pages, which list the `.md` pages underneath

Meta content goes at the top of the page, otherwise it will fail our automated checks

<pre>
   .. title:: Email | Email hosting
   .. meta::
      :description: Information regarding a wide range of email related issues
      :keywords: ukfast, email, exim, postfix, mail, dovecot, blocklist, dkim, spf
</pre>

As you'll see, the content is the same except for being wrapped in an `eval_rst` fence.

### Character length limitations for meta

- `title` - maximum of 42 characters. Don't include "| UKFast Documentation" at the end as this is will be added via the template.
- `description` - maximum of 165 characters

Your pull request will fail the automated checks without this meta content in the correct format.

## Adding elements to the page content

Most content is simple Markdown (`md`), but some features require reStructuredText (`rst`). The format is quite different compared to Markdown, and needs to be inside `eval_rst` blocks. Here are a few examples of how to add more types of content.

### Images / screenshots

Where relevant, please add screenshots to pages as image files (ideally `.png`).  This is especially useful when describing how to complete a task in MyUKFast, for instance. Please blur out any sensitive information such as account names or IP addresses, as necessary.  Most image editors will allow you to add a blurred box over the image. This looks a lot neater than using a "black marker pen" style.

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
[Go to the domain transfer in page in MyUKFast](https://my.ukfast.co.uk/domains/transfer-in.php).
```

* In reStructuredText

```rst
:doc:`/ecloud/flex/general/openstackcli`
```

This will make a hyperlink using the title of the page `/ecloud/flex/general/openstackcli` as the text.

If you wish to use text other than the heading for the section that you're linking to, use the following format:

```rst
:doc:`Custom Text</ecloud/flex/general/openstackcli>`
```

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
 * [Markdown source](https://github.com/ukfast/docs.ukfast.co.uk/edit/master/source/domains/ssl/extended_validation_ssl.md)
 * [Rendered page](https://docs.ukfast.co.uk/domains/ssl/extended_validation_ssl.html#)

#### Adding the Registered Trademark ®

Adding this:
<pre>
DDoSX\ :sup:`®`\
</pre>

Renders like this: DDoSX<sup>®</sup>

## Deploy Locally
Ensure you have `docker` and `docker-compose` installed.

```bash
git clone https://github.com/ukfast/docs.ukfast.co.uk.git ukfast_docs
cd ukfast_docs
docker-compose -f docker-compose.dev.yml up --build
```

Open a browser to 'http://localhost:80'
