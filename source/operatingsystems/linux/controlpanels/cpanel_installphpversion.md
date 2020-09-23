# Installing a PHP Version Module via EasyApache4

Before you begin to install a PHP version on your WHM/cPanel server, you need to log in to your WHM Panel.
Installing a PHP version requires you to be logged into the WHM panel as opposed to cPanel for a specific domain, this is because access to EasyApache4 is required.
EasyApache4 is used to install packages on a server-wide level and can not be used by domain level users to install package unless they have access to WHM.

![cPanel Home](files/cpanel_home.PNG)

Once you are logged into WHM, use the search box in the top left under the WHM logo to search for EasyApache4.
EasyApache4 is located under the Software category of WHM's administration features and can be also be navigated to by going following the below path:

#### Home > Software > EasyApache4

![cPanel EA4 Home](files/cpanel_easyapache4home.PNG)

When you are within WHM, click on the blue "Customize" button alongside "Currently Installed Packages" to amend the EasyApache4 Profile currently in use.
Clicking the "Customize" button on the profile currently in use will redirect you to menu in which you are able to select packages for install/uninstall accordingly.

![cPanel EA4 Apache MPM](files/cpanel_easyapache4apachempm.PNG)

To install a PHP version, click the blue "Next" and again on each page until you are on the "PHP Versions" page
Use the slider within the row of the version you require to select the version you want to install.

![cPanel EA4 PHP Version](files/cpanel_easyapache4phpversion.PNG)

```eval_rst
.. note::
   As well as marking versions for install, you can untick any version you do not require and they will be marked for uninstall by EasyApache4.
```

```eval_rst
.. warning::
   Installing and switching to a PHP version that your site/application is not compatible with may affect how it performs.
   We always recommend you check that your code is compatible with the desired PHP version before you switch to it and recommend you test any untested configurations within a development environment that could affect your application in production.
```

Once you have made the necessary changes, you can proceed through the EasyApache4 menu by clicking the blue "Next" button on each page until you reach the "Review" page.
On this page, you can review all the changes that are going to be made to the EasyApache4 profile. Happy with all the changes? You can apply the changes by clicking the "Provision" button.

![cPanel EA4 Review](files/cpanel_easyapache4review.PNG)

You will then be redirected to the final page in which will include an output window of the processes that EasyApache4 does to action your requested changes.
Once the process has finished, click the "Done" button to close your EasyApache4 session and return to the main EasyApache4 page.

![cPanel EA4 Done](files/cpanel_easyapache4done.PNG)

Using this guide, you have successfully installed a PHP version using EasyApache4!

```eval_rst
  .. title:: Installing an Apache Module via EasyApache4
  .. meta::
     :title: Installing an Apache Module via EasyApache4
     :description:  A guide to installing an Apache Module via EasyApache4
     :keywords: ukfast, php, version easy, easyapache, easyapache4, cpanel, install
