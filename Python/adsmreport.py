#!/usr/bin/env python
#
# Get backup status from Yale ADSM web site and mail it
#
import urllib,string,os,tempfile
from sys import exit

# who gets the mail
mailto = 'mark.wogahn@yale.edu'
# what name does the server know us by? Check the dsm.sys
# for NODEname
hostname = 'data1.wss.yale.edu'

staturl = 'http://130.132.83.187/cgi-bin/perlscp10?nodename=%s' % hostname
histurl = 'http://130.132.83.187/cgi-bin/perlscp36?nodename=%s&history=Backup+History' % hostname

try:
    statdata = urllib.urlopen(staturl).read()
    histdata = urllib.urlopen(histurl).read()
except IOError:
    print "URL not valid"
    exit(1)
    
#write the data to a text file for lynx to translate
f = open('/tmp/adsmreport.html','w')
f.write(statdata)
f.write(histdata)
f.close()

# let lynx do it's thing...
f = os.popen('lynx -dump /tmp/adsmreport.html').read()

# strip out the crap
start1 = string.find(f,'Response')
stop1 = string.find(f,'Occupancy')
start2 = string.find(f,'Scheduled Start')
stop2 = string.find(f,'Created')

# make a mail message and send it
temp = tempfile.mktemp()
wtemp = open(temp,'w')
wtemp.write(f[start1:stop1])
wtemp.write(f[start2:stop2])
wtemp.close()
os.system('mail %s -s "ADSM backup report for %s" < %s' % (mailto,hostname,temp))
os.remove(temp)
