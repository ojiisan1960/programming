#!/usr/bin/env python2
#
# 
import os

def checker(cmd, host):
#	print 'Doing %s to %s' % (cmd,host)
	data = os.popen('%s %s' % (cmd , host))
	status = os.wait()[1]
	if status > 0:
	    print "%s must be dead" % host
	else:
	    print "%s is okay" % host

ping='ping  -c2 -w2'
hosts = ['cyndra','supermax','b-ko','a-ko','sashimi']

for host in hosts:

	checker(ping, host)

