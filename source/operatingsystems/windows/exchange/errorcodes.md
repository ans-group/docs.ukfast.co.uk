# Error Codes

## 4.4.2

### 4.4.2 Message submission rate for this client has exceeded the configured limit

Essentially, you are trying to send an email to too many people at once


You can see the Receive Connector settings by runing the following:

```powershell
  Get-ReceiveConnector | ft Name, MessageRateLimit
```

You will see something like this:

```console
  Name                                                        MessageRateLimit

  ----                                                        ----------------

  Default EXCH                                                20

  Client Proxy EXCH                                           5

  Default Frontend CLIENT-ACCESS                              Unlimited
```

This can then be changed with the following commands:

```powershell
  Set-ReceiveConnector -Identity 'Default EXCH' -MessageRateLimit 1000
  Set-ReceiveConnector -Identity 'Client Proxy EXCH' -MessageRateLimit 1000
```

The results:

```console
  Name                                                        MessageRateLimit

  ----                                                        ----------------

  Default EXCH                                                1000

  Client Proxy EXCH                                           1000

  Default Frontend CLIENT-ACCESS                              Unlimited
```

```eval_rst
  .. title:: Microsoft Exchange error codes | UKFast Documentation
  .. meta::
     :title: Microsoft Exchange error codes | UKFast Documentation
     :description: Information on common error codes in Microsoft Exchange
     :keywords: ukfast, windows, exchange, error, codes, diagnose, cloud, server
