Title: Using OPIE
slug: reference/committer/opie

This document covers the setup and use of OPIE (One-time Passwords In Everything). This is 
a mechanism used by the ASF that ensures that your sudo password is not erroneously intercepted
or pasted into the wrong prompt on the remote machine.

Note: FreeBSD uses `opiepasswd`, Ubuntu VM's use `ortpasswd` (part of Orthrus) instead.

All users in the wheel group (or in the $machine-sudoers in LDAP) have sudo access.
In order to use sudo, a user __must
configure OPIE__ by running `opiepasswd` on the remote machine.

# Getting an OPIE client for your computer
Using OPIE requires having an OPIE (S/Key) client on the local (trusted) machine. Some OPIE clients are:

- Debian/Ubuntu: See [this forum thread](http://ubuntuforums.org/showthread.php?t=1891356)
- Browser-based: [otp-md5 tool in JavaScript](/committer/otp-md5)
- SkeyCalc (Mac OS X)
- Orthrus (Unix-like; portable)
- FreeBSD: opiekey(1) is part of the base system
- donkey (Debian package donkey) Note: Use the '-f' option to set the hash type, usually 'donkey -f md5'

# Setting up OPIE:

1. pick a good passphrase, between 10 and 127 characters long.
2. never expose it to the net, __never type it on the remote machine__
3. run `opiepasswd` (or `ortpasswd`)on the remote machine you wish to get sudo access to.
4. that will prompt you with an otp challenge, for instance: `otp-md5 fo1834 470`
5. take that challenge string and run it __locally on your workstation__
6. enter your passphrase at the __local prompt__ in 5
7. repeat 5 and 6 until you are _certain_ you entered your pw correctly
8. paste the resulting six word response into the challenge prompt in 4. If you get a 20014 error,
    you have entered your password remotely by mistake, please contact infra if so.
9. have someone add you to the 'wheel' group
10. run sudo
11. that will prompt you for an otp challenge
12. repeat steps 5-8
13. get root


# An example:

## Remote machine you want to get sudo access to:

    foo@test-vm.apache.org# opiepasswd
    You need the response from an OTP generator.
    New secret pass phrase:
	otp-md5 499 fo4576  <-- COPY THIS STRING
	Response:
        
## Local machine:

    $ otp-md5 499 fo4576
    Using the MD5 algorithm to compute response.
    Reminder: Don't use opiekey from telnet or dial-in sessions.
    Enter secret pass phrase: foobarbaztwothirty
    WERE GAIL THUG CEIL VIE TWO  <-- COPY THESE WORDS
    
## Remote machine:
    
        Response: WERE GAIL THUG CEIL VIE TWO
    root@test-vm.apache.org #

## Video Tutorial

  <video controls src="https://home.apache.org/~gmcdonald/using_opie_orthrus.mov"><a href="https://home.apache.org/~gmcdonald/using_opie_orthrus.mov">Setting up Orthrus using SKeyCalc on Mac</a>
</video>
