# What kind of attacks does a WAF prevent?

The Web Application Firewall behaves like a DROP-by-default firewall.  Applications are trained based on acceptable input, for example - the symbols `<`, `|` or `..` are not supposed to be part of a URL.

Given the whitelisting design used by UKFast WAFs, we benefit from the ability to prevent against new attack techniques even before a new "signature" is generated, deployed, and enforced - providing zero-day protection by default in many instances.

## Typical attack vectors a WAF protects you from (based on [OWASP](https://www.owasp.org/index.php/Main_Page) top 10 vulnerabilities):

 - <b>Injection:</b> The most common injections are SQL related, even though SQL is not the only language used. It entails injecting SQL language into, for instance, a web form. 
 - <b>Broken Authentication and Session Management:</b> The easiest example involves an URL containing session identifiers, which one sends to a friend via email. If the server does not check a complementary element, the second person will be able to use the account of the first person as if he or she was logged in.
 - <b>Cross Site SCripting (XSS):</b> Often called XSS, those attacks are among the easiest ones to set up. The concept is formidably simple: to make a website process JavaScript where there should be none.
 - <b>Insecure Direct Object References:</b> It is frequent for a website to include in a page resources that came from another data frame of reference. This has to be done through the mediation of a secure access or a filtration, to avoid the inclusion of unauthorized resources to be included.
 - <b>Security misconfiguration:</b> This category is very large since it covers many subjects. Are services up to date? Well protected by strong enough passwords? Are configurations adjusted to prevent important information from being divulged or mistakenly accessible?
 - <b>Sensitive data exposure:</b> OWASP emphasizes on data encoding, if data is sensitive it must be protected to avoid clear access, all sensitive data must not be accessible from the outside.
 - <b>Missing Function Level Access Control:</b> The basic idea is to never rely on security implemented on the client’s side, security and it's mechanisms should be handled in a controlled environment: On the server.
 - <b>Cross-Site Request Forgery (CSRF):</b> It is a flaw that will affect web applications (website, mobile application, etc…) whose functionalities are known (like adding a user account, changing a password, adding files) to known systems such as WordPress, this techniques requires an element of social engineering.
 - <b>Using Components with Known Vulnerabilities:</b> When someone uses a component with known vulnerabilities, you must expect an attacker to use it. It is important to understand that software that is not vulnerable at some point might become vulnerable the next day...
 - <b>Unvalidated redirects and forward:</b> This category covers attacks that are lead during redirects. Typically, 30x HTTP codes are used to redirect a user from a page to another, depending on some parameters. If the destination URL of the redirect is put as a parameter in the original page URL, then an attacker could modify this redirection by changing the URL which was put as a parameter
 
## Threat Intelligence:

Due to statistical data we collect and analyse we are able to identify bad actors and we generate IP based block lists based on the this data, learn from one or few and the community benefits.

Data can be gathered by analyzing HTTP status codes which can identify one technique (amongst others) called "fuzzing" - Fuzzing is the art of automatic bug finding, and it's role is to find software implementation faults, and identify them if possible. This allows us to build up a database of blacklist strings to deploy and block known bad traffic as early as possible.

An example: You have a PHPMyAdmin interface in public facing environment. This is not recommended and there could be many reasons for this, misconfiguration, forgotten "temporary fix" etc.. Scanners are looking for targets like this all the time scaning IP's / hostnames day and night. While the vast majority of our protection comes in the form of a whitelist, having blacklist signatures reporting information to us provides us with vital intelligence, even if you do not run PHPMyAdmin for example, the requests will still be detected and we will build up our known scanners lists in a bid to clean up traffic going through to your webservers.
