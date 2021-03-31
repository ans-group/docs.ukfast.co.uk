# Terminology and style guide

If you'd like to contribute to the UKFast Docs site then please write / produce your content in-line with this guide. Note your content may be subject to modification before or after publication.

## Terminology

Please use the following terms correctly and consistently:

| Correct term      | Examples of incorrect terms                                         | Notes                                                                        |
| ----------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| MyUKFast          | MyUKFast portal, MyUKFast client area, the client portal            | Include an embedded link to <https://my.ukfast.co.uk> at least once on page  |
| server            | device, machine                                                     |                                                                              |
| virtual machine   | virtual server                                                      | If abbreviating to "VM" then put "virtual machine (VM)" first time on page   |
| eCloud            | <nospell>ecloud, Ecloud</nospell>                                   |                                                                              |
| FASTdesk          | <nospell>Fastdesk, DaaS, Daas</nospell>                             |                                                                              |
| FASTdrive         | <nospell>Fastdrive</nospell>                                        |                                                                              |
| FASTcloudbackup   | <nospell>Fastcloudbackup, Fast cloudbackup</nospell>                |                                                                              |
| Webcelerator      | <nospell>Web celerator, Web acceleration, Web Accelerator</nospell> | Abbreviation to "Webcel" is OK                                               |

## Top-level categories

The top-level categories are as set out below.  Please do not create a new top-level category without checking first.

| Category                        | Content included                               |
| ------------------------------- | --------------------------------------------------------- |
| Cloud                           | UKFast's cloud products, cloud guidance                                                           |
| Desktop and office solutions    | UKFast's products such as FASTdesk, FASTdrive                                                     |
| Security                        | UKFast security products, general security guidance                                               |
| Domains and DNS Management      | UKFast products for managing domains and DNS, plus general guidance                               |
| Backups and Disaster Recovery   | UKFast products for backup and DR, plus general guidance                                          |
| Networking                      | Networking guidance and principles, including load balancing etc.                                 |
| Monitoring and usage management | UKFast monitoring products, plus general guidance                                                 |
| Operating systems               | Guidance relating to Linux and Windows, various "how-to" guides                                   |
| Other technologies              | Guidance relating to non-UKFast technologies and software such as WordPress, MySQL, Magento etc.  |

## Sub-Category layout

You're welcome to create a new subcategory, for example in relation to a UKFast product or service, or a third party technology where we have some useful guidance or best practise to share.  Where appropriate, please try to structure categories as follows:

1. Include a short introduction (even if just a single sentence) in the category `index.rst` file, so readers don't have to click any further to find out what it's about.
2. Then have a "General Information" page.
3. Next, a "Getting Started" guide - this is especially important if talking about a product, whether from UKFast or a third party.
4. You'll probably need a few product or topic-specific pages.
5. Always include a "Troubleshooting" page.  What are the common problems people run into, and how can they be solved?
6. Consider a "Technical information" page if it's likely readers/customers may need detailed technical knowledge of the product
7. Link to `ukfast.co.uk`, other UKFast Docs pages, and external websites as necessary.  Certainly try not to replicate content already covered on other UKFast Docs pages, just link to the relevant page.

The [FASTcloudbackup category](/source/dr-ha/fastcloudbackup) is a good example of how to structure a category.

```eval_rst
   .. title:: How to contribute to the UKFast Docs site
   .. meta::
      :description: How to contribute to the UKFast Docs site
```
