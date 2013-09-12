maildir2mbox.py
===============

(C) 2013 by [Damir Cavar](http://cavar.me/damir/)

I used this idea:


[Maildir to Mbox](http://yergler.net/projects/one-off/maildir-to-mbox/)


Python implementation of a script for the conversion of most recent Evolution maildir folders to Thunderbird mbox files.

Converts most recent Evolution maildir mails to the Thunderbird mbox format.

Create for example a folder tbmboxes, and replace in the following commandline ``myaccount`` with your account name:

Usage:


``./maildir2mbox.py /home/myaccount/.local/evolution/mail/local ./tbmboxes``


Create in Thunderbird a folder in your local mail and copy all the content from tbmboxes to this folder. Restart Thunderbird and check the files and folders for consistancy.
