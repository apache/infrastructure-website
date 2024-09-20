Title: Working in `lists.apache.org` 
license: https://www.apache.org/licenses/LICENSE-2.0

In `lists.apache.org` you can browse, search for, and read emails on mailing lists of The ASF.

  - Without logging in, you can access email in public ASF mailing lists.
  - If you have logged in:
      - if you are an ASF Member, you can access all ASF mailing lists.
      - if you are not an ASF Member but are on the PMC of a project, you can access, in addition to the public lists, the private lists of that project.
   
If you have logged in, and depending on your status as noted above, you can respond to email threads and create new messages in the email list you are currently viewing. The user interface does not have controls for these actions; instead, there are shortcut keys:

  - `H`: Display the help window.
  - `C`: Start a new email thread in the current list.
  - `R`: Reply to the current email thread.
  - `S`: Go to the search bar.
  - `Escape`: Hide modal dialogues or collapse the current thread.
  - In list view:
    - `right arrow`: Move down the current list to display the next-older bunch of emails.
    - `left arrow`: Move up the current list to display the next-newer bunch of emails.

## Searching
To display your search options, click the down-arrow at the right of the `search` field.

  - Opt to search in
    - the current list
    - all the lists of this domain; that is, if you are looking at any Apache Royale list, you can search at the same time all the email lists of `royale.apache.org` to which you have access.
    - all The ASF's email lists to which you have access.
  - You can restrict the search to
    - a specific date range
    - the author of the email
    - a keyword in the title of the email
    - the recipient of the email (a group or individual)
    - a keyword within the body of the email

## If the email you sent does not appear
The email system does not use what is in the `From` field; instead it looks at the envelope `sender`, so it is important to make sure you are using an account that appears in your LDAP record when you compose email intended for an ASF list. 

You can review and update your LDAP record at <a href="https://selfserve.apache.org/identity.html" target="_blank">selfserve.apache.org/identity.html</a>.

If you used an address that is part of your LDAP record and the message has not yet appeared, it is possible the email is awaiting moderation. Ask the PMC of the project to which you were writing if the project's email moderators are active.
