#!/usr/bin/env python
#
# fooling with command line args 

import sys ,string

print 'you entered',len(sys.argv),' arguments'
print 'they were:', str(sys.argv) # str just turns the list into a string
			          # so we can print it
#tapecmd = sys.argv[1]
#tapenum = sys.argv[2]

#cmdstring = "%s %s" % (tapecmd,tapenum)

#print cmdstring

cmd = " ".join(sys.argv[1:])

print cmd
