#!/usr/bin/env python2.2
#
# read the maillog and just give me yale info
# print out the headings 

#start ->message deferral detail
check =['message deferral detail',
'message bounce detail (by relay)',
'message reject detail',
'Recipient address rejected: Relay access denied',
#'Sender address rejected: Access denied',
'smtp delivery failures',
'connection refused',
'connection timed out',
'network is unreachable',
'no route to host',
'read timeout',
'server dropped connection',
'server refused mail service',
'Warnings',
'postsuper',
'qmgr',
'Fatal Errors',
'Panics',
'Master daemon messages']
# stop ->Per-Day Traffic Summary

f = open('maillog').read()
start = f.find('message deferral detail')
stop = f.find('Per-Day Traffic Summary')

sep = '-'*80
trimmed = f[start:stop]
for line in trimmed.splitlines():
    if line.find('yale') >=0:
	print line
    for msg in check:
	if line.find(msg) >=0:
	    print sep
	    print line
