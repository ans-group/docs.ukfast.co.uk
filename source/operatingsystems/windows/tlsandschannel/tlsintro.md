# TLS/SSL protocols and the Schannel SSP

On Windows systems, all TLS/SSL negotiation is handled by the Microsoft Secure Channel, or _Schannel_ provider native to Windows. The Schannel provider is a Microsoft proprietary system which differs from alternatives such as OpenSSL in a number of ways. You can find a basic comparison at the external link [here](https://en.wikipedia.org/wiki/Comparison_of_TLS_implementations).

The following information aims to provide a basic understanding of cipher suites, TLS and SSL protocols, and best practices in web-facing environments. The idea being that you then apply these insights to your server or solution, providing a secure environment for your users.

## SSL/TLS Protocols

In the simplest terms, these protocols provide a secure connection, or "tunnel", on which a client and server can communicate. Any observer outside of this tunnel trying to intercept traffic, will only be able to see the encrypted packets, and not the actual data within.

SSL stands for _Secure Sockets Layer_, and TLS stands for _Transport Layer Security_. Nowadays, SSL and early TLS protocols (SSL 2, SSL 3, TLS 1.0) are considered obsolete and you will always want to use later TLS protocols where possible. You should also be aware that today it is very common for the terms "SSL" and "TLS" to be used interchangeably when discussing security protocols on the Internet.

TLS 1.2 is currently the industry standard for secure communication, with TLS 1.3 in the early stages of adoption, having only very recently been formally ratified as a standard.


 ### So what is the difference between a SSL/TLS protocol and a cipher suite?

+ Think of TLS as a framework that allows security to be implemented in a certain way. It doesn't directly define how the data is encrypted and what type of key exchange is used. That is the job of the cipher suite.

+ A cipher suite can be thought of as a collection of building blocks called primitives. Each primitive does nothing on its own, but can be combined with others along with additional parameters to form a cipher suit. A cipher suite essentially defines how security is going to be implemented for that connection.

**Both ends of the connection need to agree on the cipher suite to use during the TLS handshake. This means that both parties need to have at least one supported cipher in common or else the connection cannot be established.**

For a more comprehensive overview of Transport Layer Security, consider checking the the Wikipedia page [here](https://en.wikipedia.org/wiki/Transport_Layer_Security).

We will now look at some [TLS considerations for Windows Web Servers](/operatingsystems/windows/tlsandschannel/webserverrecommendations).

```eval_rst
   .. title:: TLS protocols and Schannel
   .. meta::
      :title: TLS protocols and Schannel | ANS Documentation
      :description: Introduction to TLS protocols and cipher suites
      :keywords: SSL, TLS, ukfast, Schannel, IIS
```
