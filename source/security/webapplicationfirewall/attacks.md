# What kind of attacks does a WAF prevent?

The Web Application Firewall behaves like a DROP-by-default firewall.  Applications are trained based on acceptable input, for example - the symbols `<`, `|` or `..` are not supposed to be part of a URL.

Given the whitelisting design used by UKFast WAFs, we benefit from the ability to prevent against new attack techniques even before a new "signature" is generated, deployed, and enforced - providing zero-day protection by default in many instances.

## Typical attack vectors a WAF protects you from (based on [OWASP](https://www.owasp.org/index.php/Main_Page) top 10 vulnerabilities):

 - <b>Injection:</b> The most common injections are SQL related, even though SQL is not the only language used. It entails injecting SQL language into, for instance, a web form.
 - <b>Broken Authentication and Session Management:</b> The simplest example involves a URL containing session identifiers, which one sends to a friend via email. If the server does not check a complementary element, the second person will be able to use the account of the first person as if he or she was logged in.
 - <b>Cross Site SCripting (XSS):</b> Often called XSS, those attacks are among the easiest ones to set up. The concept is formidably simple: to make a website process JavaScript where there should be none.
 - <b>Insecure Direct Object References:</b> It is common for a page on a website to include resources from another data frame of reference. This has to be done through the mediation of a secure access or a filtration, to avoid unauthorised resources being included.
 - <b>Security misconfiguration:</b> This category is very large since it covers many subjects. Are services up to date? Well protected by strong enough passwords? Are configurations adjusted to prevent important information from being divulged or mistakenly accessible?
 - <b>Sensitive data exposure:</b> OWASP guidance on data encoding states that any sensitive data must be protected to avoid clear access, and no sensitive data should be accessible from the outside.
 - <b>Missing Function Level Access Control:</b> The basic idea is to never rely on security implemented on the client’s side; security and it's mechanisms should be handled in a controlled environment i.e. on the server.
 - <b>Cross-Site Request Forgery (CSRF):</b> This is a flaw that will affect web applications whose functionalities are known -  such as adding a user account, changing a password, adding files to known systems such as WordPress. This technique requires an element of social engineering.
 - <b>Using Components with Known Vulnerabilities:</b> If using a component with known vulnerabilities in your environment, you must expect an attacker to use it. It is important to understand that software that is not known to be vulnerable right now may become vulnerable in the future.
 - <b>Unvalidated redirects and forward:</b> This category covers attacks that are led during redirects. Typically, 30x HTTP codes are used to redirect a user from a page to another, depending on some parameters. If the destination URL of the redirect is put as a parameter in the original page URL, then an attacker could modify this redirection by changing the URL which was put as a parameter

## Threat Intelligence

Due to the statistical data UKFast collects and analyses, we are able to identify bad actors and generate IP-based block lists. Data can be gathered by analyzing HTTP status codes to find software implementation faults, which allows us to build up a database of blacklist strings to deploy and block known bad traffic as early as possible.

Here's an example: You may have a PHPMyAdmin interface in public facing environment. This is not recommended, but could be present due to a misconfiguration, or a forgotten "temporary fix". Scanners are looking for targets like this all the time by scanning IP addresses / hostnames continually. While the vast majority of our protection comes in the form of a whitelist, having blacklist signatures reporting information to UKFast provides us with vital intelligence, and allows us to clean up the traffic going through to your webservers.



```eval_rst
.. meta::
     :title: Preventing application attacks with a WAF | UKFast Documentation
     :description: General information on the attacks a UKFast WAF can help prevent
     :keywords: ukfast, ddosx, web application firewall, waf, owasp, owasp top 10
```
