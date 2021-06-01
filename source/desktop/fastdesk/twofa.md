# FastDesk Two-Factor Authentication

UKFast are partnering with Cisco Duo Security for 2FA because it is easy to use and integrates well with the FastDesk platform. Cisco Duo security protects the FastDesk environment by using a second source of validation, like a phone, to verify a users identity before granting access.

```eval_rst
.. note::

  Two-Factor Authentication is licensed on a per user basis.

```

## Two-Factor Authentication Registration

The registration process is through the web portal (only) and this can be implemented in batches as you wish as opposed to all or nothing.

Once UKFast activate Duo for a user, upon their next log in, they will be asked by Duo to enrol.  To do this, they select if they are using a Mobile Phone or a Tablet. For mobiles, the user enters their phone number and confirm it is the correct phone number.

Next, they specify if you are using an iPhone or an Android or a Windows Phone. Next, Duo signposts the user to the correct app store where they can download Duo. Once installed, they confirm they have installed Duo on their device. Next, they scan the QR Code on the screen from using the Duo app on their device.

Next, Duo will show that the account is now linked and the registration process is complete. Once registration is complete, you will be able to choose the web portal or the Citrix Workspace application as usual.

## General usage

Day to day, when a user enters their password as normal, they will be asked to select an authentication method. Users simply click "send me a push". The user will get a notification on their 2FA enabled device. When they open up the notification, they will get an `"Allow" or "Deny"` option. Users will simply select `Allow` and it will log them in as usual.


## Two-Factor Authentication Administration

From an administration point of view, UKFast will act as the administrator of your Duo account. This means Duo bypasses will be completed by UKFast Support in the situation where a user has locked themselves out. This also means we will be able to add & remove phones as well as any other administrative tasks that need completing.

Please note, the only way a user can request a bypass of Duo is if they are listed on the account ([MyUKFast Portal](https://my.ukfast.co.uk/login) or if they have someone listed on the account request a bypass. Anyone not listed on the account will not be able to request a bypass.

```eval_rst
.. note::

  In relation to roll out, please let your Onboarding engineer know if you would like this rolled out immediately or at a later date.

```

```eval_rst
   .. title:: FastDesk | FastDesk: Two-Factor Authentication Administration
   .. meta::
      :title: Two-Factor Authentication Administration | UKFast Documentation
      :description: Information guide on the process of enabling Two-Factor Authentication on FastDesk
      :keywords: FastDesk, Citrix, ukfast, VDI, Citrix Receiver, Windows, Workspace Application, Password, Change, Reset, Web, Portal, 2FA, Two-Factor
```
