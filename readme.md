# Welcome to the UKFast Documentation Repository

All the documentation is published on https://docs.ukfast.co.uk/ -

If you would like to contribute a guide or amendment to an existing one, please fork the repository and submit a pull request.

To get started, please visit:
- the "how to contribute" guide - https://github.com/ukfast/docs.ukfast.co.uk/blob/master/contribute.md
- the terminology and style guide https://github.com/ukfast/docs.ukfast.co.uk/blob/master/guide.md

## IMPORTANT:  Adding meta content to pages

Every time you add a new page to docs.ukfast, or even edit an existing page, you will need to ensure the correct meta content is added **at the bottom** of the file.  This meta content determines how the page is displayed in search engine results, and is crucial for the overall performance of the website from an SEO perspective.  Your pull request will fail the automated checks without this meta content (correctly formatted).

The code needs to be in RST, and will look as per the example below.  Please note there are character limitations we must adhere to for the `title` and `description` fields.

- `title` - maximum of 65 characters, including the "| UKFast Documentation" at the end (please always add this, which helps ensure the title is unique across docs.ukfast and ukfast.co.uk)

- `description` - maximum of 165 characters

```  
 ```eval_rst
   .. meta::
      :title: Creating an eCloud Flex instance | UKFast Documentation
      :description: Detailed guidance on creating OpenStack instances on eCloud Flex
      :keywords: openstack, ecloud flex, ukfast, nova, instance, virtual machine, vm, 
 

