# Welcome to the UKFast Documentation Repository

All the documentation is published on https://docs.ukfast.co.uk/ -

If you would like to contribute a guide or amendment to an existing one, please fork the repository and submit a pull request.

To get started, please visit:
- [the "how to contribute" guide](https://github.com/ukfast/docs.ukfast.co.uk/blob/master/contribute.md)
- [the terminology and style guide](https://github.com/ukfast/docs.ukfast.co.uk/blob/master/guide.md)


## Page Construction and Key Elements

### Naming and Path

Please ensure pages and folders are easy to read and sensibly structured. 
Please keep the page urls lowercase and use hyphens instead of spaces. e.g.

- /desktop/fastdesk/getting-started/windows.html


### Navigation, Page Heading and Meta 

When adding a new page these elements need to be considered to help site readability, usability, navigation and search results. Here's info on what each does, how to set them and some guidelines.

#### Page Heading (H1)

Sets the main heading for the page 

<img src="https://user-images.githubusercontent.com/30502984/86182420-d9c66d00-bb27-11ea-929f-5b4025c6e6b1.png" width="500">

To set 

###### within `.md` files (normal content pages)

Add as first piece of content

```
# Transferring a Domain to UKFast
```

###### within `index.rst` files (category index pages, which list the .md pages underneath)

Add to top of file

```
======================
Domain Name Management
======================
```

The h1 tag is the title of the article and should give the reader a strong sense of what they are going to read. Should be around 20 - 70 characters but length is not forced. 


#### Page Navigation and Breadcrumb

**By default** - the page navigation and breadcrumb is populated from the Page Heading and often this is perfectly fine. But sometimes a longer page heading is better for the user, but will fill up the nav with long sentences or repeated words that are not needed inside a nav tree format. In these cases it's better to set the nav item specifically. 

Example Custom Navigtation 

![image](https://user-images.githubusercontent.com/30502984/86183731-902b5180-bb2a-11ea-826b-6172fabd6236.png)

###### only within `index.rst` files 

```
.. toctree::
   :maxdepth: 1

   Transfering to UKFast <transferin>
   Transfering from UKFast <transferout>
   Changing Nameservers <changingnameservers>
   DNS Propagation <dnspropagation>
 ```


#### Page Meta Title

This meta content determines how the page is displayed in search engine results, is crucial for the overall performance of the website from an SEO perspective and helps the user with history, bookmarks and the site search.

Appearance on Google

<img src="https://user-images.githubusercontent.com/30502984/86184852-e1d4db80-bb2c-11ea-82d7-7ac5938aa705.png" width="500">

Use in the browser

<img src="https://user-images.githubusercontent.com/30502984/86185226-c0282400-bb2d-11ea-9eeb-a086c17d2a45.png" width="500">

The meta title is used in the search and displayed to the user in the site search results

<img src="https://user-images.githubusercontent.com/30502984/86186022-d6cf7a80-bb2f-11ea-80c0-94ac1342e28e.png" width="500">

In many cases the meta title can be the same as the Page Heading, but there are character length limitations we must adhere to so may require amending to be shorter. 

Also give the content a description which can help search results, but page content is more important. 

##### For `.md` files (normal content pages)

Please note spacing/indents are important so copy this template *

Meta content goes at the bottom of the file

<pre>
```eval_rst
   .. title:: Creating an eCloud Flex instance
   .. meta::
      :description: Detailed guidance on creating OpenStack instances on eCloud Flex
      :keywords: openstack, ecloud flex, ukfast, nova, instance, virtual machine, vm
```
</pre>

##### For `index.rst` files (category index pages, which list the .md pages underneath

Meta content goes at the top of the page otherwise it will fail Travis checks

<pre>
   .. title:: Email | Email hosting 
   .. meta::
      :description: Information regarding a wide range of email related issues
      :keywords: ukfast, email, exim, postfix, mail, dovecot, blocklist, dkim, spf
</pre>

(So same as .md files but not included within eval_rst)

Character Length Limitations for Meta

- `title` - maximum of 42 characters, don't include "| UKFast Documentation" at the end as this is will be added via the template.
- `description` - maximum of 165 characters

Your pull request will fail the automated Travis checks without this meta content in the correct format.


## Adding elements to the page content

Most content is simple markdown, but some features require ReStructuredText (rst) which uses quite different syntax than Markdown that need to be inside `eval_rst` blocks. Here are a few examples of how to add more types of content.

### Images / screenshots

Where relevant please add screenshots to pages as image files (ideally .png).  This is especially useful when describing how to complete a task in MyUKFast.  If appropriate please blur out any sensitive information such as account names or IP addresses.  Most image editors will allow you to add a blurred box over the image - this looks a lot neater than using a "black marker pen" style, like @simon.saffidine once tried to get away with.

Given the following structure:

```
.
├── document.md
├── files
│   ├── image.png
```

We can include `image.png` in `document.md` using markdown as below (with `someimage` becoming the alt text):

```
![someimage](files/image.png)
```

Or using reStructuredText (to control height/width) as below:

<pre>
```eval_rst

.. image:: files/image.png
   :width: 400
```
</pre>

Example image, the text preceeding becomes the Alt text

### Tables

Tables need to be in RST format otherwise they won't display properly when published (it will look fine in Git, but will look horrible when published, trust me). There are free tools that will generate RST for you, http://www.tablesgenerator.com/text_tables# is good.

This is an example which works. Note the requirement to wrap in the `eval_rst` block.
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

<pre>
:doc:`/ecloud/flex/general/openstackcli`
</pre>

This will make a hyperlinks using the title of the page `/ecloud/flex/general/openstackcli` as the text.

If you wish to use text other than the heading for the section that you’re linking to, use the following format:

```
:doc:`Custom Text</ecloud/flex/general/openstackcli>` 
```

For external links use:

```
[Go to the domain transfer in page in MyUKFast](https://my.ukfast.co.uk/domains/transfer-in.php).
```

**Link Text Tip**: Avoid using words like 'link' 'Click Here', 'Here' as the linking text. These are harder to pick out for the user and offer no idea of where the link will take them,  without forcing them to reading the preceeding content which makes it harder. The text should give a good idea to the user where it will take them when reading it alone.  



#### Adding Notes, Info, Warning, etc.

These must be done using RST, and the format is like this:
<pre>
```eval_rst
.. note::

   Sectigo also provide an online EV click-through as an alternative. This is available on request.

```
</pre>

See `/domains/ssl/Extended_Validation_SSL` as an example [Page on Site](https://docs.ukfast.co.uk/domains/ssl/Extended_Validation_SSL.html#) | [Mark Down](https://github.com/ukfast/docs.ukfast.co.uk/edit/master/source/domains/ssl/Extended_Validation_SSL.md)


#### Adding the Registered Trademark ®

Adding this:
<pre>
DDoSx\ :sup:`®`\
</pre>

Renders like this: DDoSx<sup>®</sup>


## Deploy Locally
Ensure you have docker and docker-compose installed.

```bash
git clone https://github.com/ukfast/docs.ukfast.co.uk.git ukfast_docs
cd ukfast_docs
docker-compose -f docker-compose.dev.yml up --build
```

Open a browser to 'http://localhost:80'
