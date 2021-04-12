Title: WordPress CMS acceleration and optamization
Date: 2011-04-09 23:00
Author: Predrag TASEVSKI - Pece
Tags: acceleration, optamization, simmulation of attacks and defence, wordpress
Slug: wordpress-cms-acceleration-and-optamization

PURPOSE
=======

</p>

The goal of this laboratory test is to evaluate speed-up solution for
already mounted clean, by default wordpress CMS platform. The measures
were made by custom script for Linux operating system, in our case the
server side is Ubuntu server 10.04 LTS running on 32 bit system with
512MB Ram and testing platform Fedora 14 for more details see section
appendixes.

</p>

The laboratory task is to assist anyone else to be able to perform
optimization in easy meaner to their blog, homepage, magazine, etc.
without any advantage of technical knowledge.

</p>

Presenting stepwise solution with installing firstly wordpress
optimization cache plugin, secondary installing PHP solution for
increasing the acceleration performance of the server and changing the
permalinks settings to the CMS platform for higher optimization. All of
the above solutions are free open source, and are taking care of the low
budget.

</p>

In addition providing measurement results with different scenarios will
help us to get wide picture of how affective was optimization.

</p>

METHODS
=======

</p>

Optimization of the access to wordpress CMS platform is done in behalf
of three different scenarios have been proved while performance is
getting slightly higher. Test script is measuring the response time of
the link provided and it is recording the results in a text file. Which
contains the three attends respondent time of the server. For each
method we will provide the results in analyses section.

</p>

The following steps should be done on the server side.

</p>

METHOD 1
--------

</p>

Installing procedure [WP-Super-Cache Installation], first method of
wordpress plugin: WP Super Cache Version 0.9.9.9

</p>

<div class="highlight">

    In a terminal please type the following lines:wget -c http://downloads.wordpress.org/plugin/wp-super-cache.0.9.9.9.zipsudo apt-get install unzipunzip wp-super-cache.0.9.9.9.zipmv /home/[user]/wp-super-cache /var/www/wordpress/plugins

</div>

</p>

In wordpress administration link:
[http://192.168.56.102/wordpress/](http://192.168.56.102/wordpress/wp-admin)

</p>

[wp-admin](http://192.168.56.102/wordpress/wp-admin), log in with the
credentials, from the panel select *Plugins* -\> *WP-Super-Cache* -\>
*Activate*. After the activation is done, go to *Settings* -\>
*WP-Super-Cache*, on the first tab activate the cache by selecting the
On cache and on the Advance tab select only the “(Recommended)”
settings. After your done, select *Update Settings* and on the bottom of
the page you can see a red text that needs to be copy in one of the
files that is located on the server. Connect to your server by FTP
client and locate the *.htaccess* file on the wordpress directory and
open it and paste the following lines and save the file:

</p>

<div class="highlight">

    # BEGIN WPSuperCache &lt;IfModule mod_rewrite.c&gt;RewriteEngine On RewriteBase /wordpress/AddDefaultCharset UTF-8RewriteCond %{REQUEST_URI} !^.*[^/]$RewriteCond %{REQUEST_URI} !^.*//.*$ RewriteCond %{REQUEST_METHOD} !POST RewriteCond %{QUERY_STRING} !.*=.*RewriteCond %{HTTP:Cookie} !^.*(comment_author_|wordpress_logged_in|wp-postpass_).*$RewriteCond %{HTTP:X-Wap-Profile} !^[a-z0-9\"]+ [NC]RewriteCond %{HTTP:Profile} !^[a-z0-9\"]+ [NC]RewriteCond %{HTTP_USER_AGENT} !^.*(2.0\ MMP|240x320|400X240|AvantGo|BlackBerry|Blazer| Cellphone|Danger|DoCoMo|Elaine/3.0|Eu$ RewriteCond %{HTTP_user_agent} !^(w3c\ |w3c-|acs-|alav|alca|amoi|audi|avan|benq|bird| blac|blaz|brew|cell|cldc|cmd-|dang|doco$ RewriteCond %{HTTP:Accept-Encoding} gzip RewriteCond %{DOCUMENT_ROOT}/wordpress/wp-content/cache/supercache/% {HTTP_HOST}/wordpress/$1/index.html.gz -f RewriteRule ^(.*)"/wordpress/wp-content/cache/supercache/%{HTTP_HOST}/wordpress/ $1/index.html.gz" [L] RewriteCond %{REQUEST_URI} !^.*[^/]$RewriteCond %{REQUEST_URI} !^.*//.*$ RewriteCond %{REQUEST_METHOD} !POST RewriteCond %{QUERY_STRING} !.*=.*RewriteCond %{HTTP:Cookie} !^.*(comment_author_|wordpress_logged_in|wp-postpass_).*$RewriteCond %{HTTP:X-Wap-Profile} !^[a-z0-9\"]+ [NC]RewriteCond %{HTTP:Profile} !^[a-z0-9\"]+ [NC]RewriteCond %{HTTP_USER_AGENT} !^.*(2.0\ MMP|240x320|400X240|AvantGo|BlackBerry|Blazer| Cellphone|Danger|DoCoMo|Elaine/3.0|Eu$ RewriteCond %{HTTP_user_agent} !^(w3c\ |w3c-|acs-|alav|alca|amoi|audi|avan|benq|bird| blac|blaz|brew|cell|cldc|cmd-|dang|doco$ RewriteCond %{DOCUMENT_ROOT}/wordpress/wp-content/cache/supercache/% {HTTP_HOST}/wordpress/$1/index.html -f RewriteRule ^(.*) "/wordpress/wp-content/cache/supercache/%{HTTP_HOST}/wordpress/ $1/index.html" [L] &lt;/IfModule&gt;# END WPSuperCache

</div>

</p>

METHOD 2
--------

</p>

The second approach is to install an PHP accelerator and optimizer
[EAccelerator Installing from source]. The main goal is to increases the
performance of PHP scripts by caching them in their compiled state.
Which will augment the acceleration applied with method 1.

</p>

Therefore, please follow the steps to install from source code
eAccelerator [2].

</p>

<div class="highlight">

    sudo apt-get install php-devwget -c http://ignum.dl.sourceforge.net/project/eaccelerator/eaccelerator/eAccelerator%200.9.6.1/eaccelerator-0.9.6.1.tar.bz2tar xvfj eaccelerator-0.9.6.1.tar.bz2cd eaccelerator-0.9.6.1phpize./configuremakesudo make installsudo cp /eaccelerator-0.9.6.1 /etc/apache2/php.inisudo mkdir /tmp/eacceleratorsudo chmod 0777 /tmp/eacceleratorsudo /etc/init.d/apache2 restart

</div>

</p>

After you have completed the above steps it is good way to test the php
if the eaccelerator is working and correctly installed. In any case,
please create a file called *info.php* on your wordpress directory with
the following code inside:

</p>

<div class="highlight">

    <?php phpinfo(); >

</div>

</p>

Access the link to your server vie the link
http://192.168.56.102/wordpress/info.php. If you see the configuration
information and details of PHP, the quickest way is to search for
eaccelerator, and if the result is positive, most lightly you have
installed eaccelerator correctly.

</p>

METHOD 3
--------

</p>

After we have completed the first and second methods it is time to grow
the interactiveness of our wordpress project. Therefore, we will change
setting to wordpress configuration where will speed-up the performance
[Using Permalinks]. If can still add more optimization and acceleration
applications, yet this laboratory report is performed only with three
easy and maintained steps.

</p>

Please log in to the wordpress administration panel, and on *Settings*
-\> *Permalinks* select *Default*. After the step is done, then we need
to edit the *.htaccess* file and add the following lines at the end of
the file and please save it:

</p>

<div class="highlight">

    # BEGIN WordPressIfModule mod_rewrite.c&gt;RewriteRule ^index\.php$ - [L]RewriteCond %{REQUEST_FILENAME} !-fRewriteCond %{REQUEST_FILENAME} !-dRewriteRule . /wordpress/index.php [L]&lt;/IfModule&gt;# END WordPress</pre>

</div>

</p>

ANALYSIS
========

</p>

After completing each one of the method we should perform analysis of
the system, were it will provide results of performance speed and can
compare it if it is utter to improve the effectiveness of wordpress.
Please refer to the appendix 3 to get the code of the script.

</p>

Meanwhile the below show the results served pages per/second with three
sets from the automatically created file from the custom script, named
*results\_lab2.txt*.

</p>

<table>
</p>
<p>
<thead>
</p>
<p>
<tr>
</p>
<p>
<th>
</th>
</p>
<p>
<th align="center">
Set1

</th>
</p>
<p>
<th align="center">
Set2

</th>
</p>
<p>
<th align="center">
Set3

</th>
</p>
<p>
<th align="right">
Avg

</th>
</p>
<p>
</tr>
</p>
<p>
</thead>
</p>
<p>
<tbody>
</p>
<p>
<tr>
</p>
<p>
<td>
wordpress default

</td>
</p>
<p>
<td align="center">
3.15

</td>
</p>
<p>
<td align="center">
3.7

</td>
</p>
<p>
<td align="center">
3.84

</td>
</p>
<p>
<td align="right">
3.56

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td>
WP WP-super-cache + eaccelerator

</td>
</p>
<p>
<td align="center">
26.48

</td>
</p>
<p>
<td align="center">
44.34

</td>
</p>
<p>
<td align="center">
45.68

</td>
</p>
<p>
<td align="right">
38.83

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td>
WP WP-super-cache + eaccelerator

</td>
</p>
<p>
<td align="center">
148.46

</td>
</p>
<p>
<td align="center">
173.03

</td>
</p>
<p>
<td align="center">
132.57

</td>
</p>
<p>
<td align="right">
151.35

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td>
.htaccess default permalink + wp-super-cache + eaccelerator

</td>
</p>
<p>
<td align="center">
158.57

</td>
</p>
<p>
<td align="center">
1734.11

</td>
</p>
<p>
<td align="center">
117.03

</td>
</p>
<p>
<td align="right">
136.57

</td>
</p>
<p>
</tr>
</p>
<p>
</tbody>
</p>
<p>
</table>
</p>

CONCLUSION
==========

</p>

From the analysis above we can see that performance has increased and
wordpress project is more affectively respondent to our needs.

</p>

Illustrations shows that wordpress as a default setting, clean installed
and configure response with 3.15, 3.70 and 3.84 pages/per-second, which
is not good enough to satisfaction. Similar to, after installation and
configuration of wordpress plugin WP-Super-Cache we that notice that the
performance slightly has grown but still the performance doesn’t
satisfied higher. However after implying the second method, installing
eaccelerator the results drastically increased. From the above
illustration we can see that the different methods produce different set
results. Thus increasing changes performing different methods vs sets of
pages/per-second are specified in the illustration 1.

</p>

Finally the results were expected and demonstrating example how we can
increase the addictiveness of wordpress performance and increase the
respondent time pages view per/second.

</p>

However, if we need to get higher effectiveness and response time for
wordpress than should consider apply nginx[3] server and third party
projects, applications to increase the optimization of wordpress. For
instance good tutorial is on following blog [Howto hginx+php].

</p>

APPENDIXES
==========

</p>

Appendix 1 is for installation process of Ubuntu Server 10.04 LTS and
wordpress, mysql installation, other appendix 2 is for virtual machines
configuration. The last appendix 4 is the custom script that will help
us to perform the analysis of the system.

</p>

APPENDIX 1
----------

</p>

-   Installation media: Ubuntu 10.04 LTS 32bit iso image;
-   HW: Virtualbox, 1CPU 32bit, 512MB RAM, 8GB HD (dynamic allocation);
-   NIC1 NAT;
-   NIC2 host only (for ssh and http access from host);
-   Language used in installation process: English and country Estonia;
-   Keyboard Layout English;
-   Hostname: pece
-   Partition methods: Guided, use entire disk
-   Username: pece
-   no http proxy
-   Default applications
-   sudo apt-get install lamp phpmyadmin
-   wget -c http://wordpress.org/latest.tar.gz
-   tar xvjf latest.tar.gz
-   sudo cp wordpress /var/www/wordpress
-   sudo nano /var/www/wordpress/wp-config.php
-   Change the settings to your needs

</p>

APPENDIX 2
----------

</p>

Ubuntu Server 10.04 LTS 32bit – Server

</p>

-   Base Memory: 512 MB
-   Acceleration: VT-x/AMD-V, Nested Paging
-   Display – Video memory: 12 MB
-   Storage: SATA Controller, Port 0: 8 GB
-   Network:
    -   Adapter 1: Intel PRO/1000 MT Desktop (NAT)
    -   Adapter 2: Inter PRO/1000 MT Desktop (Host-only adapter,
        „VirtualBox Host-Only Enternet Adapter“)

    </p>
    <p>

</p>

Security Fedora 14 32 bit – Client

- base Memory: 512 MB

- Acceleration: VT-x/AMD-V, Nested Paging

- Display – Video memory: 12 MB

- Storage: SATA Controller, Port 0: 8 GB

- Network:

- Adapter 1: Adapter 1: Parvirtualized Network (NAT)

- Adapter 2: Adapter 2: Inter PRO/1000 MT Desktop (Host-only
adapter,„VirtualBox Host- Only Enternet Adapter“)

</p>
</p>

APPENDIX 3
----------

</p>

File called lab2\_test.sh. Content of the file:

</p>

+--------------------------------------+--------------------------------------+
| <div class="linenodiv">              | <div class="highlight">              |
|                                      |                                      |
|      1 2 3 4 5 6 7 8 910111213141516 |     #!/bin/bash#Author Margus Ernits |
| 1718192021222324                     | #License GPLCONCURENCY=10RESULTS_FIL |
|                                      | E=results.txtif [ $# -ne 1 ]; thenec |
| </div>                               | ho "Use $0 http://yourwordpressIP/yo |
|                                      | urwordpresssite/"echo "for example:" |
|                                      | echo "$0 http://192.168.56.102/wordp |
|                                      | ress/"exit 1fiecho "give name for th |
|                                      | is test"echo "for example: wordpress |
|                                      |  with supercache"read TEST_NAMEtest  |
|                                      | -e ${RESULTS_FILE} || echo "Test Nam |
|                                      | e,Set 1,Set 2,Set 3"&gt;${RESULTS_FI |
|                                      | LE}RESULTS=$TEST_NAMEfor setno in $( |
|                                      | seq 1 3); doecho "Set $setno ..."SET |
|                                      | _RESULT=$(ab -c$CONCURENCY -n200 $1| |
|                                      | grep "Requests per second:"|cut -f2- |
|                                      | d:|cut -f1 -d'[')RESULTS=${RESULTS}, |
|                                      | $SET_RESULTdoneecho "$RESULTS"&gt;&g |
|                                      | t;${RESULTS_FILE}echo "test: $TEST_N |
|                                      | AME done"                            |
|                                      |                                      |
|                                      | </div>                               |
|                                      |                                      |
|                                      | </p>                                 |
|                                      | <p>                                  |
+--------------------------------------+--------------------------------------+

</p>

Bibliography
============

</p>

WP-Super-Cache Installation: WP, Installation, 2011,
[http://wordpress.org/extend/plugins/wp-super-cache/installation/](http://wordpress.org/extend/plugins/wp-super-%20cache/installation/ "http://wordpress.org/extend/plugins/wp-super- cache/installation/")

</p>

EAccelerator Installing from source: eAccelerator project, Installation
from source code, 2011, <http://eaccelerator.net/wiki/InstallFromSource>

</p>

Using Permalinks: WordPress, Using Permalinks, 2011,
<http://codex.wordpress.org/Using_Permalinks>

</p>

Howto hginx+php: joneslee85, Howto nginx + php5 + mysql + phpmyadmin +
ubuntu shortest setup, 2010,
[http://joneslee85.wordpress.com/2010/02/28/howto-nginx-php5-mysql-phpmyadmin-ubuntu-shortest-setup/](http://joneslee85.wordpress.com/2010/02/28/howto-nginx-php5-mysql-phpmyadmin-%20ubuntu-shortest-setup/ "http://joneslee85.wordpress.com/2010/02/28/howto-nginx-php5-mysql-phpmyadmin-ubuntu-shortest-setup/")

</p>

Footnotes
=========

</p>

[1] WP Super Cache –
[](http://wordpress.org/extend/plugins/wp-super-cache/</a></p></p><p><p>[2]%20eAccelerator%20-%20<a%20href=)

</p>

[2] eAccelerator - <http://eaccelerator.net/>

</p>

[3] Nginx Inc – http://nginx.net/

</p>

