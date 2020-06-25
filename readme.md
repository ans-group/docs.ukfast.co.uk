# Welcome to the UKFast Documentation Repository

All the documentation is published on https://docs.ukfast.co.uk/ -

If you would like to contribute a guide or amendment to an existing one, please fork the repository and submit a pull request.

To get started, please visit:
- [the "how to contribute" guide](https://github.com/ukfast/docs.ukfast.co.uk/blob/master/contribute.md)
- [the terminology and style guide](https://github.com/ukfast/docs.ukfast.co.uk/blob/master/guide.md)


### Adding Pages

Please ensure pages and folders are easy to read and sensibly structured. 
Please keep the page urls lowercase and use hyphens instead of spaces. e.g.

- /desktop/fastdesk/getting-started/windows.html


#### Adding meta content to pages 

Every time you add a new page to docs.ukfast or even edit an existing page, you will need to ensure the correct meta content is added.

This meta content determines how the page is displayed in search engine results, is crucial for the overall performance of the website from an SEO perspective and helps the user with history, bookmarks and saerchign the site.

Your pull request will fail the automated Travis checks without this meta content in the correct format.

Please note there are character length limitations we must adhere to for the `title` and `description` fields.

##### Meta Required 

- `title` - maximum of 42 characters, don't include "| UKFast Documentation" at the end as this is will be added via the template.

- `description` - maximum of 165 characters

- `keywords` - (optional) list of relating keywords

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

### Adding screenshots to pages

Where relevant please add screenshots to pages as image files (ideally .png).  This is especially useful when describing how to complete a task in MyUKFast.  If appropriate please blur out any sensitive information such as account names or IP addresses.  Most image editors will allow you to add a blurred box over the image - this looks a lot neater than using a "black marker pen" style, like @simon.saffidine once tried to get away with.

### Adding tables

Tables need to be in RST format otherwise they won't display properly when published (it will look fine in Git, but will look horrible when published, trust me). There are free tools that will generate RST for you, [this one](http://www.tablesgenerator.com/text_tables#) is good.

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

### Adding into `eval_rst` blocks

ReStructuredText (rst) uses quite different syntax than Markdown. Here are a few examples of how to use it

#### Hyperlinks

The easiest form to add them is like this:

<pre>
:doc:`/ecloud/flex/general/openstackcli`
</pre>

This will make a hyperlinks using the title of the page `/ecloud/flex/general/openstackcli` as the text.

#### Adding Notes, Info, Warning, etc.

These must be done using RST, and the format is like this:
<pre>
```eval_rst
.. note::

   Sectigo also provide an online EV click-through as an alternative. This is available on request.

```
</pre>
See `/domains/ssl/Extended_Validation_SSL` as an example

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
