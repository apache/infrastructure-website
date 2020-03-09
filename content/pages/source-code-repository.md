Title: Source Code Repositories at Apache

Apache project contributors are in countries all around the world. To help them work together, projects keep their source code in an Internet-accessible revision control system, either <a href="https://subversion.apache.org/" target="_blank">Subversion (SVN)</a> or <a href="https://git-scm.com/" target="_blank">Git</a>. Apache committers have _write access_ to the repositories for their projects, so they can edit existing code and add new files. 

Everyone has _read access_ to the repositories and can download the most up-to-date development version of any project's software to review or compile. 

- If you want a stable release of the source code, download it from the <a href="https://www.apache.org/dyn/closer.cgi/" target="_blank">distribution directory</a>. 
- Only download the code directly from your project's code repository if you are participating in the development effort. The latest version of the code is what your colleagues have most recently checked in, and they may or may not have confirmed that it compiles correctly and does what they want it to do.
- If you want a release version of the project's compiled application, visit the project's website and find its download page. It may offer both stable releases and "bleeding-edge" or "nightly" builds that compile properly but include the latest, possibly-unstable, features.

## Git repositories ##
How-to guides, documentation, and a list of projects using git for revision control are at <a href="https://git.apache.org/" target="_blank">git.apache.org</a>.

## SVN repositories ##
Information about SVN is at <a href="https://subversion.apache.org/" target="_blank">the Apache SVN site</a> and <a href="http://svnbook.red-bean.com/" target="_blank">Version Control with Subversion</a>. The website provides links for _SVN clients_ you can download and install to make it easier to work with SVN.

To browse the repositories or download a few individual files, you can

- use <a href="https://svn.apache.org/viewvc/" target="_blank">viewvc</a>
- find a project repository at <a href="https://svn.apache.org/repos/asf/" target="_blank">the list of SVN repos</a>

### Command-line SVN access ###
You can check out a project repository anonymously once you have installed a SVN client. For example, to get the Spamassassin module, use:

     `$ svn checkout http://svn.apache.org/repos/asf/spamassassin/trunk spamassassin`

### Committing code through the command line ###
If you are a project committer and don't want to use a SVN client like Tortoise, you can commit your new and updated files using the command line. We use HTTPS basic authentication, so you need to specify your user name and password as part of the check-in command.

For example, if you wanted to add the file 'test.txt', you might follow these steps:

``` $ svn co https://svn.apache.org/repos/asf/excalibur/trunk/ excalibur-trunk
$ cd excalibur-trunk
$ echo "test" > test.txt
$ svn add test.txt
$ svn commit --username your-name --password your-password \
  --message "Trying out svn"
```

Apache does not support `svnserve` or `svn+ssh`.

### Configuring the SVN client ###
Committers need to properly configure their svn client. One particular issue is OS-specific line-endings for text files. When you add a new text file, especially when applying patches from Bugzilla, make sure that the line-endings are appropriate for your system, then do (for test.txt)

`svn add test.txt svn propset svn:eol-style native test.txt` 

You can configure your svn client to do that automatically for some common file types. Add the contents of <a href="https://www.apache.org/dev/svn-eol-style.txt" target="_blank">this file</a> to the bottom of your ~/.subversion/config file, normally found at:

- Windows: C:\Documents and Settings\{username}\Application Data\Subversion\config
- Windows 7: C:\Users\{username}\AppData\Roaming\Subversion\config]
- Linux & Mac OSX: ~/.subversion/config or /etc/subversion/config

You may need to set additional properties for some files. For example, apply `svn:executable=*` to script files (e.g. .bat, .cgi, .cmd, .sh) that are intended to be executed. Since not all such files are intended to be executed, do not make the executable property an automatic default.

Pay attention to the messages from your svn client when you do 'svn commit'.

**Tip**: If you use TortoiseSVN, a popular Windows GUI client that integrates with Windows Explorer, you can right click in Explorer and select TortoiseSVN - Settings, and then press the "Edit" button to update your "Subversion configuration file:". If you do not see 

     `*.c = svn:eol-style=native`

copy the above svn-eol-style.txt file's contents into the end of the config editor that appears, and save the file.

### SVN SSL server certificate ###

You can check the validity of the server certificate on the <a href="https://www.apache.org/dev/machines.html" target="_blank">Apache host keys listing</a>.







