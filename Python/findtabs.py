#!/usr/bin/env python2
# find files, search for tabs

import string,os

cmd = 'find . -name "*.py" -print'

for file in os.popen(cmd).readlines(): #run the find command
	num = 1
	name = file[:-1] # strip off '\n'
	for line in open(name).readlines():	#scan the file'
		pos = string.find(line, '\t')
		if pos >= 0:
			print name, num, pos #report tab found
			print '....', line[:-1] # [:-1] strips final "\n"
			print '....', ''*pos + '*', '\n'

		num = num+1
