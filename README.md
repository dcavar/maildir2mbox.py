maildir2mbox.py
===============

(C) 2013 by [http://cavar.me/damir/](Damir Cavar)


Python implementation of a script for the conversion of most recent Evolution maildir folders to Thunderbird mbox files.

Converts most recent Evolution maildir mails to the Thunderbird mbox format.

Create for example a folder tbmboxes, and replace in the following commandline ``myaccount`` with your account name:

Usage:

  ./maildir2mbox.py /home/myaccount/.local/evolution/mail/local ./tbmboxes

Create in Thunderbird a folder in your local mail and copy all the content from tbmboxes to this folder. Restart Thunderbird and check the files and folders for consistancy.
