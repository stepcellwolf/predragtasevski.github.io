Title: Security Programing Techniques
Date: 2012-02-21 00:00
Author: Predrag TASEVSKI - Pece
Tags: ASP.NET, bash, C#, cyber security, HQL, java, JDBC, Perl, PHP5, python, Ruby on Rail, security, security model, Unix, windows 7
Slug: security-programing-techniques

INTRODUCTION
============

</p>

The main goal of this post is to introduce the reader with the security
programing techniques into deferent program languages and operating
system security models. The post is introducing four following topics:

</p>

1.  Session storage’s in Ruby on Rail
2.  Parameterized statements into Java with JDBC, C\# with ASP.NET,
    PHP5, php-mysqli, Perl, Python and Hibernate Query Language (HQL)
3.  Unix permission model, Unix ACL and Windows 7 security model
4.  Finding all the security vulnerabilities in bash script

</p>

Each topic will be divided into own section, where at the end of each
topic we stated the reference and additional reading material. The
source code, scrips and the additional task were given by the lecture.
However this will help the readers and people interesting into
programing for further work and involvement with the above topics.

</p>

1. Session storage’s in Ruby on Rail
====================================

</p>

Session in Rails is a hash-like structure which allows you to store data
across requests. Sessions can hold any kind of data object (with some
limitations) because they store data using Data Marshalling.Session in
rails it is not a hash. Session creates new instant of session in every
time new user visit the site. Recommendation is to not store large
objects in a session and critical data should not be stored in
session.Rails way of

implementing session is:

</p>

1.  session\_id is a 32 hex character MD5 hash based upon time, random
    number and constant string. It is stored in cookie at client
    browser. Rails provides transparent support for session\_id.
2.  Session storage discussed below.

</p>

Ruby on Rails provides with many session storage option:

</p>

1.  PStore – it implements a file based persistence mechanism based on a
    Hash. User code can store hierarchies of Ruby objects (values) into
    the data store file by name (keys). An object hierarchy may be just
    a single object. User code may later read values back from the data
    store or even update data, as needed. The files that are stored are
    usually located in the tmp/sessions folder for the Rails app. The
    main downside of using the PStore is that you will have to do some
    session-pruning periodically because performance decreases as the
    number of sessions stored increases.
2.  ActiveRecordStore – keeps the session id and hash in a database
    table and saves and retrieves the hash on every request.
3.  CookieStore – it saves the session hash directly in a cookie on the
    client-side. The server retrieves the session hash from the cookie
    and eliminates the need for a session id. Cookie-based sessions are
    just faster to retrieve and process than hitting the file-system on
    every request, were it was previously. Cookies are generally limited
    to 4K in size. While not an issue for most (proper) usage of the
    session, this could be a legitimate limit for some scenarios. If
    your application abuses the session, you’ll need to decide on a
    different session store that are available. The cookie has a SHA512
    fingerprint attached and is hashed with a secret stored up on the
    server and there are, however, derivatives of CookieStore which
    encrypt the session hash, so the client cannot see it.
4.  DRbStore – it store uses distributed Ruby to store a user’s session
    data. The performance is great, but it requires a bit more setup
    than the other stores.
5.  FileStore – This store keeps the fragments on the hard disk instead
    of in memory. It works well if you have a lot of file storage and
    have outgrown the MemoryStore.
6.  MemoryStore – keeps your session data in server memory. It keeps the
    fragments in your application’s memory, which can potentially take
    up a lot of memory on your server. It is used by default, but it is
    hard to manage and scale if your application becomes popular.

</p>

**Note:** Ruby on Rail CookieStore is available only in edge rails.
PStore is the default option for stable release, whereas its CookieStore
as default for edge rails.

</p>

Reference
---------

</p>

Ruby On Rails Security Guide, From:
<http://guides.rubyonrails.org/security.html>

</p>

Sessions and cookies in Ruby on Rails, From:
[http://www.quarkruby.com/2007/10/21/sessions-and-cookies-in-ruby-on-rails\#sstorage](http://www.quarkruby.com/2007/10/21/%20sessions-and-cookies-in-ruby-on-rails#sstorage)

</p>

What’s New in Edge Rails: Cookie Based Sessions are the New Default,
From:
<http://ryandaigle.com/articles/2007/2/21/what-s-new-in-edge-rails-cookie-based-sessions>

</p>

2. Parameterized statements into Java with JDBC, C\# with ASP.NET, PHP5, php-mysqli, Perl, Python and Hibernate Query Language (HQL)
====================================================================================================================================

</p>

For this task we will take a look at the parameterized statement API-s
and we will find out and document how much does each of them protect
against the following possible misuses of SQL statements:

</p>

-   String injection (quotes, double quotes)
-   SQL statement injection (expression syntax etc)
-   Out of range integers
-   Blind SQL injection

</p>

Java with JDBC
--------------

</p>

<div class="highlight">

    PreparedStatement prep =conn.prepareStatement("SELECT * FROMUSERSWHERE USERNAME=? AND PASSWORD=?");prep.setString(1, username);prep.setString(2, password);prep.executeQuery();

</div>

</p>

There are no possibilities of string injection because of the filtering
the statements. It enables users’ input to be initially filtered
instead  of directly embedding it in the SQL statements. In this example
is that the each parameter is a scalar, not a table, where the user
input is then assigned (bound) to a parameter. It is a good idea if the
character range is limited. Another thing that can be done to avoid SQL
injection is to convert numeric values to integers before parsing them
into the SQL statement. Or using ISNUMERIC to verify that they are
integers.

</p>

C\# with ASP.NET
----------------

</p>

<div class="highlight">

    using (SqlCommand myCommand =new SqlCommand("SELECT * FROM USERSWHEREUSERNAME=@user ANDPASSWORD=HASHBYTES(’SHA1’, @pwd)",myConnection)){myCommand.Parameters.AddWithValue("@user",user);myCommand.Parameters.AddWithValue("@pwd",pass);myConnection.Open();SqlDataReader myReader =myCommand.ExecuteReader();...}

</div>

</p>

The placeholder – @user and the hashbyte value of password @pws – has
become part  if the hardcoded SQL. At runtime, the value provided by the
querystring is passed to the database along with the hardcoded SQL, and
the database will check the Username and password field as it attempts
to bind the parameter value to it. This ensures a level of strong
typing. If the parameter value is not the right type for the database
field (a string, or numeric that’s out of range for the field type), the
database will be unable to convert it to the right type and will reject
it. If the target field datatype is a string (char, nvarchar etc), the
parameter value will be “stringified” automatically, which includes
escaping single quotes. It will not form part of the SQL statement to be
executed.

</p>

PHP5
----

</p>

<div class="highlight">

    $db = new PDO(’pgsql:dbname=database’);$stmt = $db-prepare("SELECT priv FROM testUsers WHERE username=:username AND password=:password");$stmt-bindParam(’:username’, $user);$stmt-bindParam(’:password’, $pass);$stmt-execute();

</div>

</p>

In this example to protect against SQL injection, it is used an input
not directly to be  embedded in SQL statements. Instead, it is used an
parameterized statements (preferred), or user input must be carefully
escaped or filtered. This example shows and parameterized
example/statement in php v. 5 and PDO database to protect from SQL
injections and blind SQL injections.

</p>

PHP-MySQLi
----------

</p>

<div class="highlight">

    $db = new mysqli("host", "user", "pass","database");$stmt = $db - prepare("SELECT priv FROM testUsers WHERE username=? AND password=?");$stmt -  bind_param("ss", $user, $pass);$stmt - execute();

</div>

</p>

Same as above but this time it is used the vendor-specific methods; for
instance, using the mysqli extension for MySQL 4.1 and create
parameterized statements to protect from the SQL injection.

</p>

Perl
----

</p>

<div class="highlight">

    use DBI;my $db = DBI-connect(’DBI:mysql:mydatabase:host’, ’login’, ’password’);$statment = $db-&amp;amp;amp;amp;amp;gt;prepare("UPDATE players SET name = ?, score = ?, active = ? WHERE jerseyNum = ?");$rows_affected = $statment-&amp;amp;amp;amp;amp;gt;execute("Smith, Steve", 42, ’true’, 99);

</div>

</p>

Automatically “sanitize” input to parameterized SQL statements to avoid
the catastrophic  database attacks.

</p>

Python
------

</p>

<div class="highlight">

    import sqlite3db = sqlite3.connect(’:memory:’)db.execute(’update players set name=:name, score=:score,active=:active where jerseyNum=:num’, {’num’: 100, ’name’: ’John Doe’, ’active’: False, ’score’: -1})

</div>

</p>

It is parameterized statement with an example of named placeholders.
Which insure to avoid the SQL injections and database attacks.

</p>

Hibernate Query Language (HQL)
------------------------------

</p>

<div class="highlight">

    Query safeHQLQuery = session.createQuery("from Inventory where productID=:productid");safeHQLQuery.setParameter("productid", userSuppliedParameter);

</div>

</p>

Unsafe example: Query unsafeHQLQuery = session.createQuery(“from
Inventory where productID=’”+userSuppliedParameter+”‘”); The example
from left it’s used prepared statement approach because all the SQL code
stays within the application. This makes your application relatively
database independent. However, other options allow you to store all the
SQL code in the database itself, which has both security and
non-security advantages and the approach is called Stored Procedure

</p>

3. Unix permission model, Unix ACL and Windows 7 security model
===============================================================

</p>

In this topic we will describe two security set-ups that can not be
expressed with traditional Unix permission model, UNIX ACL and Windows 7
security model.

</p>

Unix permission model
---------------------

</p>

-   Giving an different permission to different users in the same group
-   Read and write permission/access to all groups, which gives and
    access to the ‘private files’, and you can gain access through a
    root account by an unwanted user, which brings and complete breach
    of the system

</p>

Unix ACL- enabled permission model
----------------------------------

</p>

-   If the user has permission over the file, he can read/write and
    delete it, which brings that it is not possible to give ‘some’
    permission to the user.
-   ACL’s are not very portable and are very hard to maintain. For
    instance good example is transferring of files with ACL’s between
    different of Unix systems is an exercise for brave person, even if
    the both file systems support them. Which brings a difficulty to
    maintain for existing files for instance backup, restore, copying,
    etc.

</p>

Windows 7 security model
------------------------

</p>

-   As a standard user you can perform an action that requires
    administrator privileges by the UAC(User Access Control), which is
    controlled by the Admin Approval Mode. It can be turn off and on.
    Every time when you need to gain an access of the administration
    privileges it will be prompt a dialog box to gain and provide the
    password for an access. Therefore in the medium settings with any
    malware could turn it off.
-   And the settings of the UAC are in medium mode not off, still brings
    an opportunity to being turn off by the malware.

</p>

4. Finding all the security vulnerabilities in bash script
==========================================================

</p>

In this topic we will find all the possible vulnerabilities into the
following bash script:

</p>

+--------------------------------------+--------------------------------------+
| <div class="linenodiv">              | <div class="highlight">              |
|                                      |                                      |
|      1 2 3 4 5 6 7 8 910111213141516 |     #!/bin/sh# remove files with nam |
| 17181920212223                       | e pattern matching regexpif [ x$1 =  |
|                                      | x ]; then# if [[ x$1 = x ]]echo -n " |
| </div>                               | Please enter directory name: "read d |
|                                      | irelsedir=$1fiif [ x$2 = x ]; then#  |
|                                      | if [[ x$2 = x ]]echo -n "Please ente |
|                                      | r pattern: "read patternelsepattern= |
|                                      | $2fifind $dir &amp;amp;amp;amp;amp;g |
|                                      | t; /tmp/listing# can use &amp;amp;am |
|                                      | p;amp;amp;gt;&amp;amp;amp;amp;amp;gt |
|                                      | ; or print the output first beforecm |
|                                      | d='rm `grep '$pattern' /tmp/listing` |
|                                      | ' #+the command is executeecho "Runn |
|                                      | ing command $cmd"eval $cmd //it conv |
|                                      | erts string in commandrm /tmp/listin |
|                                      | gexit 0                              |
|                                      |                                      |
|                                      | </div>                               |
|                                      |                                      |
|                                      | </p>                                 |
|                                      | <p>                                  |
+--------------------------------------+--------------------------------------+

</p>

We should avoid temporary file, instead we should use pipes [2]. We
should avoid eval [2].

</p>

Using the double brackets, instead of single one `[[... ]]` it is
comment on the script above [1]. \$REPLY can be used to read the
previous value of the dir and pattern variable [1]. We can use instead
of find, while read contracture (loop) [1]. Find – can be set with a
cycle, for or while to check the validation of the file and the
directory/path, also comment on the script or using
`“$pattern” /tmp/listing` [1]. No sensitization of the input, the user
can put any value and therefore, execute any command to create another
command. As we can see above the script it looks like that it is
security vulnerable. If we want to implement the security in the script
we should implement the above changes into the script.

</p>

Reference
---------

</p>

[1] Mendel Cooper, 30 April 2011. Advanced Bash-Scripting Guide; An
in-depth exploration of the art of shell scripting. Retrieved from:
<http://tldp.org/LDP/abs/html/index.html>

</p>

[2] Lecture 8 slides Scripting, Meelis Roos. Retrieved from file:
08-scripting.pdf

</p>

