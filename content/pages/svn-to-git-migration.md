Title: SVN to Git migration

SELF SERVICE
Migrating to git is self-serve now. Please request a bare (empty) git repo via https://selfserve.apache.org/ and then use svn2git to convert your svn repo to git. Once completed, you can push the new repo to gitbox.apache.org (or GitHub) and have infra set the old svn repo to read-only.

The svn authors list (required by svn2git for cloning) is at https://gitbox.apache.org/authors.txt

