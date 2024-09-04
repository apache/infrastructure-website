Title: How to submit a patch for project code
license: https://www.apache.org/licenses/LICENSE-2.0

To contribute a change or addition to existing source code:

### Using Subversion ###

See [Subversion basics](svn-basics.html)

1. Check out the latest copy of the source code from the project's code repository.
2. Change the source files to incorporate your change or addition. Make sure you provide appropriate source code documentation (like javadoc for
Java sources), and follow the project's coding conventions.
3. Check the software still compiles and runs correctly on your local machine.
4. Run any unit or regression tests the software may have.

If all this works, you can create your patch. Remove all build products and remnants (like any 'build', 'dist' or 'bin' directories) from the module tree, then build the actual patch. Here's how to do it using the command line SVN client under unix:

Apache projects prefer the unified diff format. The subversion tool creates that automatically. If you use other tools, please refer to their documentation for details on setting the diff format.

```
    # location where the modules are stored
    cd checkout</p>
<div class="codehilite"><pre><span class="c"># directory of the module</span>
<span class="n">cd</span> <span class="n">site</span>

<span class="c"># creation of the diff</span>
<span class="n">svn</span> <span class="nb">diff</span> <span class="o">&gt;</span> <span class="n">site</span><span class="p">.</span><span class="nb">patch</span>
</pre></div>
```

The Subversion client now examines all subdirectories for changed files, then compares the changed file to the one on the server. It generates the
patch.

The '&gt;' redirection results in the resulting patch being put in a text file named (in this case) `site.patch`.

With your patch generated, you need to send it to the developers. Different projects have different preferences for this. Usually you add it as an attachment to the relevant bug report in the bug tracking database. If a relevant bug report doesn't exist yet, create one.

### Using Git ###

See [Getting started with Git](git-primer.html) for general information.

The general pattern for creating and submitting a patch for a project using Git is:

0. Before you start: talk to the project team! Somebody else may be working on the same thing, or there may be some not-obvious reason why what you are proposing would take the project in a different direction from its current path. Usually, you will get a "Great! Go ahead," response; and if you find out your proposed change is not needed for some reason, you will have saved some time for some other initiative.
1. Create and download a branch of the project.
2. In that branch, on your local computer, change the source files to incorporate your change or addition. Make sure you provide appropriate source code documentation and follow the project's coding conventions.
3. Check the software still compiles and runs correctly on your local machine.
4. Run any unit or regression tests the software may have.
5. Upload your changes from your local computer to the branch you created.
6. Create a pull request to merge your branch into the trunk of the project's code.

One or more of the project's committers will review your proposed changes and, if all is well, merge them.


### In general ###

A very few projects don't use an issue tracker. In that case, send the patch as an attachment to an e-mail with a subject prefixed with "<code>[PATCH]</code>", to the appropriate development mailing list. If the patch is large, please ask before e-mailing it in case there is a better way to provide it.

Supply a different patch per issue. A patch can span multiple files but you should normally try not to fix multiple bugs in a single patch, unless those bugs are intimately related.

Be patient if your patch is not applied as fast as you'd like (open source developers are all volunteers, often doing the development in their spare time) or a developer asks you to make changes to the patch. If you do not receive any feedback in a reasonable amount of time (say, a week or two), feel free to send a follow-up e-mail to the developer list.
