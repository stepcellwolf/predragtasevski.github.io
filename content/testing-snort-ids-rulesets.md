Title: Testing SNORT – IDS rulesets
Date: 2012-03-13 00:00
Author: Predrag TASEVSKI - Pece
Tags: cyber security, DDoS, ids, internet, networking, online, Port scan, snort, snort rules, SYN flood, testing ids, vulnerability scanning
Slug: testing-snort-ids-rulesets

SCENARIO
========

</p>

The objective of this laboratory test, scenario is to create a solution
and instructions for testing an IDS^1^ systems usefulness for detecting
attacks against a wordpress site. In addition, we have to
develop/download/find/whatever a SNORT configuration (rulesets,
preprocessors, whatever) that performs better than the default
configuration in previous post. By better we mean:

</p>

-   Less false positives
-   Less false negatives
-   The objectives are contradictory so the rule of thumb is one false
    negative per 10 false positives eg. solution with 10 false positives
    and 2 false negatives is better than the solution with 100 false
    positives and 1 false negatives, but the solution with 10 false
    positives and 1 false negative is better than the solution with 1
    false positive and 2 false negatives.
-   Attack is defined by a single invocation of all the test scripts in
    a row.

</p>

Meanwhile, the new rules have to be able to detect not only the default
attacks that are set to a default snort configuration, yet they have to
be able to detect SQL injection, brute force password, apache killer
script, pytbull, etc. Furthermore, in figure 1 we are illustrating the
scenario.

</p>

Illustration 1: Illustration of Scenario

</p>

Therefore, in the proposal section we will present two proposals that
have been submitted due to this laboratory test and additionally in
result section we will highlighted the identification numbers made by
snort set new rules. In section appendixes we will provide you with more
details configuration procedures, configuration of VM’s – Virtual
Machines, attacks, etc.

</p>

Finally, closing with an conclusion and the results of best set of rules
made of the proposals.

</p>

SETUP of SNORT
==============

</p>

To setup snort in a right way, that will work for the second Host only
network please following the instruction link provided with a full
description and configuration of snort [SNORT2].

</p>

PROPOSALS
=========

</p>

In total two proposals are presented in next sub-sections.

</p>

PROPOSAL 1
----------

</p>

Add <http://www.tud.ttu.ee/~t061780/attacks/robert.rules> to your Snort.
On your Snort machine:

</p>

<div class="highlight">

    cd /etc/snort/ruleswget http://www.tud.ttu.ee/~t061780/attacks/robert.rules

</div>

</p>

Now you have the rules, add them to your snort conf file (default
/etc/snort/snort.conf). To do that inser:

</p>

`include $RULE_PATH/robert.rules` somewhere with rest of the rules after
line 800. Run Snort and test.

</p>

PROPOSAL 2
----------

</p>

Add the following rules: <http://predragtasevski.com/src/predrag.rules>.
To be able to insert the snort rules in to the snort file please double
check where it is located. You can find the location with the following
command: find / -name snort.conf Before you continue please change the
IP address to your server address on line number \#6, example alert tcp
any any -\> 192.168.56.X where x is your octet. Then to add the
following rules at the conf file do the following command:

</p>

`cat predrag.rules &amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;gt; snort.conf`

</p>

Now it is time to start or restart snort. It should work.

</p>

RESULTS
=======

</p>

After executing the above proposal we will highlight the results into
the table bellow. Result are presented from the total amount of reports,
registered alerts in the snort. This is done by help of web interface of
Basic Analysis and Security Engine in addition Analysis Console for
Intrusion Databases (ACID) project tool [ACID]. Therefore, the result
from the proposals are highlighted below:

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
<th align="right">
Attack performed

</th>
</p>
<p>
<th align="center">
Proposal number

</th>
</p>
<p>
<th align="center">
Baseline Total number of Alerts

</th>
</p>
<p>
<th align="center">
Total number of Alerts

</th>
</p>
<p>
<th align="right">
Unique Alerts

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
<td align="right">
SQL injection

</td>
</p>
<p>
<td align="center">
1

</td>
</p>
<p>
<td align="center">
0

</td>
</p>
<p>
<td align="center">
0

</td>
</p>
<p>
<td align="right">
0

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td align="right">
SQL injection

</td>
</p>
<p>
<td align="center">
2

</td>
</p>
<p>
<td align="center">
0

</td>
</p>
<p>
<td align="center">
52

</td>
</p>
<p>
<td align="right">
1

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td align="right">
Pytbull – evasion

</td>
</p>
<p>
<td align="center">
1

</td>
</p>
<p>
<td align="center">
N/A

</td>
</p>
<p>
<td align="center">
128

</td>
</p>
<p>
<td align="right">
6

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td align="right">
SQL injection + nmap

</td>
</p>
<p>
<td align="center">
Combine both

</td>
</p>
<p>
<td align="center">
N/A

</td>
</p>
<p>
<td align="center">
36

</td>
</p>
<p>
<td align="right">
5

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td align="right">
Pytbull

</td>
</p>
<p>
<td align="center">
Combine both

</td>
</p>
<p>
<td align="center">
N/A

</td>
</p>
<p>
<td align="center">
844

</td>
</p>
<p>
<td align="right">
7

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

Table 1: Details of total report numbers of alerts made by SNORT and the
different proposal rule sets. Details of the attacks conducted in the
table are presented in appendixes section.

</p>

Additionally, figure 2 is presenting the pine chart of the total number
alerts recognized by Snort.

</p>

Illustration 2: Total number of Alerts.

</p>

Secondly, figure 3 is representing the pine chart of total number of
unique alerts recognized by Snort.

</p>

Illustration 3: Total number of Unique Alerts

</p>

CONCLUSION
==========

</p>

From the above results we came to conclusion that the new applied rules
were successful and were able to recognize alerts more then the default
rule set of Snort. Meanwhile, only proposal 2 was able to recognized an
SQL injections without any additional tweaking. Although proposal 1 was
still useful, on the other hand the best solution is when we combine the
both rule sets proposals. Then the Snort is able to recognized an
significant number of total alerts and additionally for our laboratory
report more interesting is unique total number alerts.

</p>

Closing, even the default Snort rules configuration is good, yet when
you tweak it by

your own needs, you will have much better IDS system for your network.
In future it should be recommended always refer to [snort\_rules], to
gather more available advance Snort rules, made by experts. Where will
help you to configure and setup Snort IDS system to detecting attacks
against a wordpress site, etc.

</p>

APPENDIXES
==========

</p>

Appendix 1 is the configuration of the attacker virtual machine, in more
detail Blacktrack 5 distribution. Secondly, Appendix 2 is the ubuntu
wordpress configuration server and additional is the configuration and
setup process and refer links of IDS Snort virtual machine. Appendix 4,
5 and 6 are providing brief details about the attacks that were
conducted during this laboratory test.

</p>

APPENDIX 1
==========

</p>

-   Installation media: Black Track 5 GNOME 32bit iso image;
-   HW: Virtualbox, 1CPU 32bit, 512MB RAM, 8GB HD (dynamic allocation);
-   NIC1 NAT;
-   NIC2 host only (for ssh and http access from host);
-   Downloadable link: <http://www.backtrack-linux.org/downloads/>

</p>

<h1>
APPENDIX 2

</h2>
</h1>
</p>

-   Installation media: Ubuntu 10.04 32bit iso image;
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

</p>

<div class="highlight">

    sudo apt-get install lamp phpmyadminwget -c http://wordpress.org/latest.tar.gztar xvjf latest.tar.gzsudo cp wordpress /var/www/wordpresssudo nano /var/www/wordpress/wp-config.php Change the settings to your needs

</div>

</p>

APPENDIX 3
==========

</p>

-   Installation media: Ubuntu 10.04 32bit iso image;
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
-   Snort configuration and installation refer to [SNORT1] in addition,
    please refer to [SNORT2].

</p>

APPENDIX 4
==========

</p>

Here we test typical SQL- injection in URLs

Commands used:

</p>

<div class="highlight">

    wget "http://192.168.56.101/?p=1'%20OR%20'1'='1"wget "http://192.168.56.101/?p=1'%20AND%201=(SELECT%20COUNT(*)%20FROM%20tabname);%20—"

</div>

</p>

Snort by default does not detect this, where in applying the proposal 2
rules, it did detect.

</p>

APPENDIX 5
==========

</p>

To test Snort and acidbase, perform a portscan of the Snort host.

</p>

`sudo nmap -p1-65535 -sV -sS -O 192.168.56.102`

</p>

APPENDIX 6
==========

</p>

To setup pytbull it is a bit of pain, yet if you follow the rules and
the documentation it will work like shark. For documentation please
refer to [pytbull\_doc].

</p>

Bibliography
============

</p>

[SNORT2] Nick Moore, Snort 2.8.4.1 Ubuntu 9 Installation Guide, June
2009, <http://www.snort.org/assets/113/Snort_2.8.4.1_Ubuntu.pdf>

</p>

[ACID] Basic Analysis and Security Engine, Welcome to the Basic Analysis
and Security Engine (BASE) project ,
2008,<http://base.secureideas.net/about.php>

</p>

[snort\_rules]
<http://rules.emergingthreats.net/open/snort-2.9.0/rules/>

</p>

[SNORT1] kat-amsterdam, SnortIDS, December 2010,
<https://help.ubuntu.com/community/SnortIDS>

</p>

[pytbull\_doc] Sébastien Damaye, Official documentation for pytbull v1.3
-, 2011, <http://pytbull.sourceforge.net/index.php?page=documentation>

</p>

[1] IDS – Intrusion detection system

</p>

