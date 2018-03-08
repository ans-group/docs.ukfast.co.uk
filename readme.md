# Welcome to the UKFast Documentation Repository

All the documentation is published on https://docs.ukfast.co.uk/ -

If you would like to contribute a guide or amendment to an existing one, please fork the repository and submit a pull request.

To get started, please visit:
- [the "how to contribute" guide](https://github.com/ukfast/docs.ukfast.co.uk/blob/master/contribute.md)
- [the terminology and style guide](https://github.com/ukfast/docs.ukfast.co.uk/blob/master/guide.md)

## IMPORTANT:  Adding meta content to pages

Every time you add a new page to docs.ukfast, or even edit an existing page, you will need to ensure the correct meta content is added to the file as follows:

- **for `.md` files (normal pages)** - meta content goes at the bottom of the file  
- **for `index.rst` files ("category" pages, which have a number of .md pages underneath)** - meta content goes at the top of the page otherwise it will fail Travis checks

This meta content determines how the page is displayed in search engine results, and is crucial for the overall performance of the website from an SEO perspective.  Your pull request will fail the automated Travis checks without this meta content (correctly formatted).

The code needs to be in RST, and will look as per the example below.  Please note there are character limitations we must adhere to for the `title` and `description` fields.

- `title` - maximum of 65 characters, including the "| UKFast Documentation" at the end (please always add this, which helps ensure the title is unique across docs.ukfast and ukfast.co.uk)

- `description` - maximum of 165 characters

```  
 ```eval_rst
   .. meta::
      :title: Creating an eCloud Flex instance | UKFast Documentation
      :description: Detailed guidance on creating OpenStack instances on eCloud Flex
      :keywords: openstack, ecloud flex, ukfast, nova, instance, virtual machine, vm, 
 ```
 
## Adding screenshots to pages

Where relevant please add screenshots to pages as image files (ideally .png).  This is especially useful when describing how to complete a task in MyUKFast.  If appropriate please blur out any sensitive information such as account names or IP addresses.  Most image editors will allow you to add a blurred box over the image - this looks a lot neater than using a "black marker pen" style, like @simon.saffidine once tried to get away with.

## Adding tables

Tables need to be in RST format otherwise they won't display properly when published (it will look fine in Git, but will look horrible when published, trust me).  Please bold and shade the title row, take a look at [this page](https://docs.ukfast.co.uk/cloud/flex/nova/flavour_sizes.html) for a nice example, and you can see the code [here](https://raw.githubusercontent.com/ukfast/docs.ukfast.co.uk/master/source/cloud/flex/nova/flavour_sizes.md) if you want to grab and edit it for your own table.  

Alternatively there are free tools that will generate RST for you, [this one](http://www.tablesgenerator.com/text_tables#) is good
