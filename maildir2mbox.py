#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
maildir2mbox.py

(C) 2013 by Damir Cavar
http://cavar.me/damir/

Converts most recent Evolution maildir mails to the Thunderbird mbox format.

Create for example a folder tbmboxes, and replace in the following
commandline "myaccount" with your account name:

Usage:
./maildir2mbox.py /home/myaccount/.local/evolution/mail/local ./tbmboxes

Create in Thunderbird a folder in your local mail and copy all the content from
tbmboxes to this folder. Restart Thunderbird and check the files and folders
for consistancy.
"""


import sys, mailbox, email, os

ENDING = ".sbd"


def processMaildir(maildir, target):
	mdir = mailbox.Maildir(maildir, email.message_from_file)
	ofp = file(target, 'w')
	for mdir_msg in mdir:
		msg = email.message_from_string(str(mdir_msg))
		ofp.write(str(msg))
		ofp.write('\n\n')
	ofp.close()


def main(maildirpath, targetf):
	for directory, dirnames, filenames in os.walk(maildirpath):
		if "cur" in dirnames:
			prefix, fname = os.path.split(directory)
			if fname[0] == ".":
				target = os.path.join(targetf, fname[1:].replace(".", ENDING + os.path.sep))
			else:
				target = os.path.join(targetf, fname.replace(".", ENDING + os.path.sep))
			# create target directories
			targetfolder = os.path.split(target)[0]
			#print "Testing for folder:", targetfolder
			if not os.path.isdir(targetfolder):
				os.makedirs(targetfolder)
			# check for the folder files
			checkfiles = target.split(ENDING)[:-1]
			for y in range(1, len(checkfiles)):
				checkfiles[y] = checkfiles[y-1] + ENDING + checkfiles[y]
				if not os.path.isfile(checkfiles[y]):
					#print "Touching:", checkfiles[y]
					tmpf = open(checkfiles[y], "a")
					tmpf.close()
			print "Converting:", directory, "to", target
			processMaildir(directory, target)


if __name__=="__main__":
	main(sys.argv[-2], sys.argv[-1])

