Title: IP Responsibility and abuse reporting procedure
Date: 2011-03-11 00:00
Author: Predrag TASEVSKI - Pece
Tags: attacks, cyber security, DDoS, external IP, Internet Protocol addressing systems, IP addresses, malware, online, report abuse, security, security risk
Slug: ip-responsibility-and-abuse-reporting-procedure

PURPOSE
=======

</p>

The main goal of laboratory report is to identify the responsibilities
for the IP addresses below and how we can make connection to them. IP
addresses are randomly chosen by the lecture.

</p>

IP addresses:

​1. 69.163.171.238

​2. 31.44.184.101

​3. 188.72.228.69

</p>

External IP that is used for purpose of this test is following:
193.40.244.0/255 1. The ISP that provides this network is EENet2.
Organization that is behind is Tallinn Technical University, Estonia.
City location is Tallinn and the region is Harjumaa. The phone number of
my ISP is: +372 73***\**. The e-mail we should report abuse are: first
persons that is in charge: Viktor Borisevitch (e-mail:**tor at cc.ttu.ee
and phone number: +372-2-***\*46) and Andres Lepp (e-mail: l*** at
cc.ttu.ee and phone number: +372 6 **\***55). In addition, if we wont to
submit an abuse we should use both persons of network administration and
then we can submit and security incident on the following ISP e-mail:
turvas@eeenet.ee [RIPE NCC].

</p>

All in all, Method 1 and Appendix 1 describes the website, tools and
application that are used to conduct this laboratory report. In
addition, Method 2 and Appendix 2 will introduce website tools and
databases where we can check if following IP’s have been reported before
as abuse and security risk. Both methods are represented with answer and
consequences confront in the result section.

</p>

Finally the conclusion made of all collected data will be concise in
conclusion section of this report.

</p>

METHODS
=======

</p>

First method describes and demonstrates web tools that have been used to
collect the needed information from the stated IP’s addresses. Second
method is pointing out website tools and databases that can be applied
if the IP has been reported previously as a abuse, spam or security
threat.

</p>

METHOD 1
--------

</p>

Firstly, we need to collect as much as we can details about the IP
address. In Appendix 1 is showing the wholly information of the IP’s,
contact details, organization name, address, location, state, country,
technicians contact, abuse phone number, abuse e-mail, etc.

</p>

Depending on the location of IP we should make sure that not only we
know the ISP or abuse contact details, but we should know national CERT
3 agency that is in charge too. Therefore, to collect the information we
have used different web sites, agencies: [RIPENCC, LACNIC, AfriNIC,
APNIC, ARIN]. The above reference are agencies collected from IANA4.
Authority responsible for global coordination of the Internet Protocol
addressing systems [IANA].

</p>

Moreover, to have more details about the route of the IP’s we are using
command prompt in Windows 7 with the following command, where the
results are presented in Appendix 2 section:

</p>

<div class="highlight">

    tracert [0.0.0.0]To illustrate, the details information are presented in Result 1 section.

</div>

</p>

METHOD 2
--------

</p>

After we have collected the wholly information about the concrete IP
proposals, we should check if in addition those IP’s previously have
been reported as abused, spam or security threat. To complete the
following method we need to check concrete database system that is
offering following service. First that crossed on web is [MalwareURL]
which is dedicated to fighting malware, trojans and a multitude of other
web-related threats. In addition, we can check if the IP addresses are
listed in anti-spam databases. With other words blacklist check
[MyIPAddress].

</p>

RESULTS
=======

</p>

Results from Method 1 are presented in Result 1, further Method 2 is
presented in Result 2.

</p>

RESULT 1
========

</p>

For each IP are presented only the most important data details that we
need to collect for our goal. In addition, full description and details
are presented in Appendix 1. The tables bellow are illustrating the most
important information that we should look-for. In addition, the
highlighted lines are indicating the abuse e-mail box that should be
send mail too.

</p>

<div class="highlight">

    69.163.171.238OrgName: New Dream Network, LLCAddress: 417 Associated Rd.Address: PMB #257City: BreaStateProv: CAPostalCode: 92821Country: US#technician in chargeOrgTechName: Nagel, MarkOrgTechPhone: +1-714-706-4182OrgTechEmail: mna47-arin at dreamhost.com#abuse in chargeOrgAbuseName: DreamHost Abuse TeamOrgAbusePhone: +1-714-706-4182OrgAbuseEmail: abuse&nbsp; at dreamhost.comTable 131.44.184.101person: Chris Burnsaddress: Building 4>address: City West Office Parkaddress: Gelderd Roadaddress: Leeds LS12 6LXaddress: Englandphone: +44-208-901-2332#abuse e-mail: abuse-mailbox: abuse at laveconetworks.co.ukTable 288.72.228.69role: Mannesmann Arcor Network Operation Centeraddress: Arcor AG &amp; Co. KGaddress: Department TBSaddress: Otto-Volger-Str. 19address: D-65843 Sulzbach/Ts.address: Germanyphone: +49 6196 523 0864#abuse e-mailabuse-mailbox: abuse at arcor-ip.deTable 3

</div>

</p>

However, now that we know the abuse e-mail, phone number and contact
person details, still is this information enough for us. If we look in
details all of the IP’s are from different countries. Therefore we need
to find what is the national CERT agency contact details. First table is
based in USA, therefore we need to use their reporting system, which is
locate in the following link: <http://www.us-cert.gov/> . Second table
is UK, the national CERT agency link:
[www.ukcert.org.uk](http://www.ukcert.org.uk/). Third table is based in
Germany, the CERT agency link: <http://www.cert-verbund.de/>.

</p>

From the routing trace we can conclude that the first IP and the third
respond and it did not miss route trace, where in the second IP,
31.44.184.101 there is miss route trace.

</p>

That is why we will run this IP address to Method 2. Despite the fact,
still we will run the rest of IP’s in the Method 2, to be trusted that
are not in the abuse list.

</p>

RESULT 2
--------

</p>

Next step is to attempt to search the IP address to check if they have
been previously report as a abuse, trojan, malware, security threat,
etc.

</p>

To check and verify the security status we are using the service
available [MalwareURL]. Where results for 69.163.171.238 and
88.72.228.69 are with status that have not been previously reported as
abuse. On the other hand, 31.44.184.101 IP address is detected as an
security threat before. More details are presented in Appendix 3. Where
is demonstrating that the
`/404.php?type=stats&amp;affid=531&amp;subid=03&amp;iruns` has been
reported as malicious URL and it is in a blacklist of Google, MyWOT,
etc.

</p>

Not only that it is listed in the malware database list, but also if we
double check on service [MyIPAddress] that the 31.44.184.101 IP address
is listed in few blacklist which is assess by DNSBL5.

</p>

CONCLUSION
==========

</p>

In conclusion, I would like to reiterate that the concrete IP’s that we
analysis in this report are demonstrating the process and methods that
should be done in future to detect, report abuse, malware, threat,
trojan, security risk, etc. Where we should gather the detail
information, and to whom to turn the abuse. To be precise that are not
in blacklist, spam list, etc.

</p>

In spite of following IP’s: 69.163.171.238 and 88.72.228.69, from
performing methods and delivering results are safe and secure, still
think can be exploited in easy manners. The opposite, IP address
31.44.184.101 it has been already report infected as malicious code from
few blacklist providers. When checking the DNS, host name is linking to
UK company that deals with IP Transit. For further information please
check the following link: <http://www.laveconetworks.co.uk/>.

</p>

In general, hope that laboratory report and the analyse will help to
anyone else to guide them for future use.

</p>

APPENDIXES
==========

</p>

Appendix 1 is list of details collected from service. Appendix 2 is
trace route details. Where Appendix 3 is the result collected from the
black list database.

</p>

Because of large content please download
[[PDF](http://predragtasevski.com/pdf/Predrag_Tasevski_Lab3_Report_IP_responsibility.pdf)]

</p>

Bibliography
============

</p>

RIPE NCC: RIPE NCC, Data & Tools, 2011,
<https://www.ripe.net/data-tools>

</p>

LACNIC: Internet Address Registry for Latin America and the Caribbean,
REGISTRATION SERVICES , <http://lacnic.net/cgi-bin/lacnic/whois?lg=EN>

</p>

AfriNIC: AfriNIC LTD, Query the AfriNIC Whois Database, 2011,
href="http://www.afrinic.net/cgi-bin/whois"
target="\_blank"\>http://www.afrinic.net/cgi-bin/whois</a>

</p>

APNIC: APNIC, APNIC – Query the APNIC Whois Database, 2011,
<http://wq.apnic.net/apnic-bin/whois.pl>

</p>

ARIN: ARIN, WHOIS-RWS, 2011,
[http://whois.arin.net](http://whois.arin.net/)

</p>

IANA: IANA, Number Resources, 2011, <http://www.iana.org/numbers/>

</p>

MalwareURL: The MalwareURL Team, The MalwareURL Team, 2011,
[http://www.malwareurl.com](http://www.malwareurl.com/)

</p>

MyIPAddress: What Is My IP Address, Blacklist Check, 2011,
<http://whatismyipaddress.com/blacklist-check>

</p>

Footnotes:
==========

</p>

[1] I will not show my own IP address

</p>

[2] EENet – <http://www.eenet.ee/EENet/>

</p>

[3] CERT – Computer Emergency Response Team

</p>

[4] IANA – Internet Assigned Numbers Authority – <http://www.iana.org/>

</p>

[5] DNSBL – Domain Name System Blacklist

</p>

-   Changed on purpose, not to disclose the exposure

</p>
