#!/usr/bin/env python2.2
#
# read the maillog and just give me yale info
# print out the headings 

check = ['smtp delivery failures',
'connection refused',
'connection timed out',
'network is unreachable',
'no route to host',
'read timeout',
'server dropped connection',
'server refused mail service']

#f = open('maillog').read()
# read from stdin
import sys
f = sys.stdin.read()
start = f.find('smtp delivery failures')
stop = f.find('Per-Hour Traffic Summary')

sep = '-'*80
trimmed = f[start:stop]
for line in trimmed.splitlines():
    for msg in check:
	if line.find(msg) >=0:
	    print sep
	    print line
#Warnings
    if line.find('Warnings') >=0:
	print sep
	print line
#Fatal Errors
    if line.find('Fatal Errors') >=0:
	print sep
	print line
#Panics
    if line.find('Panics') >=0:
	print sep
	print line
#Yale
    if line.find('yale') >=0:
	print line
