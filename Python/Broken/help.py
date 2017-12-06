#! /usr/bin/env python
import sys
#bad if ?
if '-h' in sys.argv or '--help' in sys.argv or '--help' in sys.argv: 
 	   print '''
	   help.py--does nothing useful (yet)
	   options: -h, -help, or --help-display this help
	   Copyright (c) Jacek Artymiak, 2000 '''
    	   sys.exit(0)
else:
	print 'I dont recognize this option' 
#sys.exit(0)
