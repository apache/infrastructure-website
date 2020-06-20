Title: Writing a good bug report

When you run into an issue
Why You Should Read This

Simply put, the more effectively you report a bug, the more likely an engineer will actually fix it.
These bug writing guidelines are an attempt at a general tutorial on writing effective bug reports for novice bug writers; not every sentence may precisely apply to your software project.


How to Write a Useful Bug Report

Useful bug reports are ones that get bugs fixed. A useful bug report normally has two qualities:

Reproducible. If an engineer can't see it or conclusively prove that it exists, the engineer will probably stamp it "WORKSFORME" or "INVALID", and move on to the next bug. Every detail you can provide helps.

Specific. The quicker the engineer can isolate the issue to a specific problem, the more likely it'll be expediently fixed. (If a programmer or tester has to decypher a bug, they spend more time cursing the submitter than fixing or testing the problem.)
Let's say the application you're testing is a web browser. You crash at foo.com, and want to write up a bug report:

BAD: "My browser crashed. I think I was on foo.com. My computer uses Windows. I think that this is a really bad problem and you should fix it now. By the way, your icons really suck. Nobody will use your software if you keep those ugly icons. Oh, and my grandmother's home page doesn't look right, either, it's all messed up. Good luck."

GOOD: "I crashed each time when I went to foo.com, using the 10.28.99 build on a Win NT 4.0 (Service Pack 5) system. I also rebooted into Linux, and reproduced this problem using the 10.28.99 Linux build.

It again crashed each time upon drawing the Foo banner at the top of the page. I broke apart the page, and discovered that the following image link will crash the application reproducibly, unless you remove the "border=0" attribute:

<IMG SRC="http://foo.com/images/topics/topicfoos.gif" width=34 height=44 border=0 alt="News">"



How to Enter your Useful Bug Report into Bugzilla:

Before you enter your bug, use the Bugzilla Query Page to determine whether the defect you've discovered is a known bug, and has already been reported. (If your bug is the 37th duplicate of a known issue, you're more likely to annoy the engineer. Annoyed engineers fix fewer bugs.)

Next, be sure that you've reproduced your bug using a recent build. (Engineers tend to be most interested in problems afflicting the code base that they're actively working on, rather than those in a code base that's hundreds of bug fixes obsolete.)

If you've discovered a new bug using a current build, report it in Bugzilla:

From your Bugzilla main page, choose "Enter a new bug".
Select the product that you've found a bug in.
Enter your E-mail address, Password, and press the "Login" button. (If you don't yet have a password, leave the password text box empty, and press the "E-mail me a password" button instead. You'll receive an E-mail message with your password shortly.)
Now, fill out the form. Here's what it all means:

Where did you find the bug?

Product: In which product did you find the bug?
You just filled this out on the last page.

Version: In which product version did you find the bug?
If applicable.

Component: In which component does the bug exist?
Bugzilla requires that you select a component to enter a bug. (If they all look meaningless, click on the Component link, which links to descriptions of each component, to help you make the best choice.)

Platform: On which hardware platform did you find this bug? (e.g. Macintosh, SGI, Sun, PC.)
If you know the bug happens on all hardware platforms, choose 'All'. Otherwise, select the platform that you found the bug on, or "Other" if your platform isn't listed.

OS: On which Operating System (OS) did you find this bug? (e.g. Linux, Windows NT, Mac OS 8.5.)
If you know the bug happens on all OSs, choose 'All'. Otherwise, select the OS that you found the bug on, or "Other" if your OS isn't listed.


How important is the bug?

Severity: How damaging is the bug?
This item defaults to 'normal'. (To determine the most appropriate severity for a particular bug, click on the Severity link for a full explanation of each choice, from Critical to Enhancement.)


Who will be following up on the bug?

Assigned To: Which engineer should be responsible for fixing this bug?
Bugzilla will automatically assign the bug to a default engineer upon submitting a bug report; the text box exists to allow you to manually assign it to a different engineer. (To see the list of default engineers for each component, click on the Component link.)

Cc: Who else should receive e-mail updates on changes to this bug?
List the full e-mail addresses of other individuals who should receive an e-mail update upon every change to the bug report. You can enter as many e-mail addresses as you'd like; e-mail addresses must be separated by commas, with no spaces between the addresses.


What else can you tell the engineer about the bug?

URL: On what URL did you discover this bug?
If you encountered the bug on a particular URL, please provide it (or, them) here. If you've isolated the bug to a specific HTML snippet, please also provide a URL for that, too.

Summary: How would you describe the bug, in approximately 60 or fewer characters?
A good summary should quickly and uniquely identify a bug report. Otherwise, developers cannot meaningfully query by bug summary, and will often fail to pay attention to your bug report when reviewing a 10 page bug list.

A summary of "PCMCIA install fails on Tosh Tecra 780DVD w/ 3c589C" is a useful title. "Software fails" or "install problem" would be examples of a bad title.


Description: What else can you tell the engineer about this bug?
Please provide as detailed of a problem diagnosis in this field as possible.

Where applicable, using the following bug report template will help ensure that all relevant information comes through:

Overview Description: More detailed expansion of summary.

Drag-selecting any page crashes Mac builds in NSGetFactory
Steps to Reproduce: The minimal set of steps necessary to trigger the bug. Include any special setup steps.

1) View any web page. (I used the default sample page, 
   resource:/res/samples/test0.html)
2) Drag-select the page. (Specifically, while holding down the 
   mouse button, drag the mouse pointer downwards from any point in 
   the browser's content region to the bottom of the browser's 
   content region.)
Actual Results: What the application did after performing the above steps.

The application crashed. Stack crawl appended below from MacsBug.
Expected Results: What the application should have done, were the bug not present.

The window should scroll downwards. Scrolled content should 
be selected. (Or, at least, the application should not crash.)
Build Date & Platform: Date and platform of the build that you first encountered the bug in.

11/2/99 build on Mac OS (Checked Viewer & Apprunner)
Additional Builds and Platforms: Whether or not the bug takes place on other platforms or browsers.

 - Occurs On
        Seamonkey (11/2/99 build on Windows NT 4.0)

 - Doesn't Occur On
        Seamonkey (11/4/99 build on Red Hat Linux; feature not supported)
        Internet Explorer 5.0 (RTM build on Windows NT 4.0)
        Netscape Communicator 4.5 (RTM build on Mac OS)
Additional Information: Any other debugging information. For crashing bugs:

Win32: if you receive a Dr. Watson error, please note the type of the crash, and the module that the application crashed in. (e.g. access violation in apprunner.exe)
Mac OS: if you're running MacsBug, please provide the results of a how and an sc.
Unix: please provide a minimized stack trace, which can be generated by typing gdb apprunner core into a shell prompt.
*** MACSBUG STACK CRAWL OF CRASH (Mac OS)

Calling chain using A6/R1 links
 Back chain  ISA  Caller
 00000000    PPC  0BA85E74  
 03AEFD80    PPC  0B742248  
 03AEFD30    PPC  0B50FDDC  NSGetFactory+027FC
PowerPC unmapped memory exception at 0B512BD0 NSGetFactory+055F0
You're done!

After double-checking your entries for any possible errors, press the "Commit" button, and your bug report will now be in the Bugzilla database.


(Thanks to Claudius Gayle, Peter Mock, Chris Pratt, Tom Schutter, and Chris Yeh for contributing to this document. Constructive suggestions welcome.)
