# Remove CA Certificate from System Trust Store
Root Certificate Authority (CA) certificates can and do expire. Typically, alternative CAs are available on the system, and often it is the case that a system package update will remove the older expired certificates (for example, the `ca-certificates` package).
Though infrequent, sometimes an expired Root CA might cause issues (for example, OpenSSL 1.0.2x) and needs to be manually removed from your server trust store.
##  CentOS 7

```eval_rst
.. note::
   For CentOS7, there is now an updated package that removes this expired certificate:
   ``yum install ca-certificates``
   You can then check and confirm this is fixed with:
   ``rpm -q --changelog ca-certificates | grep "DST ROOT CA X3" -B4``
   ``* Tue Sep 14 2021 Bob Relyea <rrelyea@redhat.com> - 2021.2.50-72
   - Fix expired certificate.
   -    Removing:
   -     # Certificate "DST Root CA X3"``
```

Backup the trust store
```bash
cp -i /etc/pki/tls/certs/ca-bundle.crt ~/ca-bundle.crt-backup
```
Identify the CA certificate
```bash
trust list
```
Add certificate to blacklist directory
```bash
trust dump --filter "pkcs11:id=%c4%a7%b1%a4%7b%2c%71%fa%db%e1%4b%90%75%ff%c4%15%60%85%89%10" | openssl x509 | tee /etc/pki/ca-trust/source/blacklist/DST-Root-CA-X3.pem
```
Update the system trust store
```bash
update-ca-trust extract
```
Verify removal
```bash
diff ~/ca-bundle.crt-backup /etc/pki/tls/certs/ca-bundle.crt
```
Sample Output
```bash
$ diff ~/ca-bundle.crt-backup /etc/pki/tls/certs/ca-bundle.crt
860,881d859
< # DST Root CA X3
< -----BEGIN CERTIFICATE-----
< MIIDSjCCAjKgAwIBAgIQRK+wgNajJ7qJMDmGLvhAazANBgkqhkiG9w0BAQUFADA/
< MSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT
< DkRTVCBSb290IENBIFgzMB4XDTAwMDkzMDIxMTIxOVoXDTIxMDkzMDE0MDExNVow
< PzEkMCIGA1UEChMbRGlnaXRhbCBTaWduYXR1cmUgVHJ1c3QgQ28uMRcwFQYDVQQD
< Ew5EU1QgUm9vdCBDQSBYMzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
< AN+v6ZdQCINXtMxiZfaQguzH0yxrMMpb7NnDfcdAwRgUi+DoM3ZJKuM/IUmTrE4O
< rz5Iy2Xu/NMhD2XSKtkyj4zl93ewEnu1lcCJo6m67XMuegwGMoOifooUMM0RoOEq
< OLl5CjH9UL2AZd+3UWODyOKIYepLYYHsUmu5ouJLGiifSKOeDNoJjj4XLh7dIN9b
< xiqKqy69cK3FCxolkHRyxXtqqzTWMIn/5WgTe1QLyNau7Fqckh49ZLOMxt+/yUFw
< 7BZy1SbsOFU5Q9D8/RhcQPGX69Wam40dutolucbY38EVAjqr2m7xPi71XAicPNaD
< aeQQmxkqtilX4+U9m5/wAl0CAwEAAaNCMEAwDwYDVR0TAQH/BAUwAwEB/zAOBgNV
< HQ8BAf8EBAMCAQYwHQYDVR0OBBYEFMSnsaR7LHH62+FLkHX/xBVghYkQMA0GCSqG
< SIb3DQEBBQUAA4IBAQCjGiybFwBcqR7uKGY3Or+Dxz9LwwmglSBd49lZRNI+DT69
< ikugdB/OEIKcdBodfpga3csTS7MgROSR6cz8faXbauX+5v3gTt23ADq1cEmv8uXr
< AvHRAosZy5Q6XkjEGB5YGV8eAlrwDPGxrancWYaLbumR9YbK+rlmM6pZW87ipxZz
< R8srzJmwN0jP41ZL9c8PDHIyh8bwRLtTcm1D9SZImlJnt1ir/md2cXjbDaJWFBM5
< JDGFoqgCWjBH4d1QB7wCCZAA62RjYJsWvIjJEubSfZGL+T0yjWW06XyxV3bqxbYo
< Ob8VZRzI9neWagqNdwvYkQsEjgfbKbYK7p2CNTUQ
< -----END CERTIFICATE-----
<
```
```eval_rst
   .. title:: SSL | Remove CA Certificate from System Trust Store
   .. meta::
      :title: SSL |  Remove CA Certificate from System Trust Store | ANS Documentation
      :description: Manually Remove CA Certificates from System Trust Store
      :keywords: letsencrypt, lets, let's, root, CA, ssl, linux, certificate, expired, trust store
```
