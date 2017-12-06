#!/usr/bin/env python
#
# Check for new rpms on ftp2

import urllib,os,tempfile
from string import find

startstring = 'channel'
lynxcom = 'lynx -dump -force_html -nolist -width=200'

def main():
    """Get the listings and print em"""
    url = 'http://ftp.wss.yale.edu/rpm2html/ByDate.html'
    # make a temp file for the html crud
    mytemp = tempfile.mktemp()
    htmlcrud = open(mytemp,'w')
    htmlcrud.write(urllib.urlopen(url).read())
    # close file
    htmlcrud.close()
    # use lynx to read file 
    text = os.popen('%s %s' % (lynxcom, mytemp)).read() 
    start = find(text,startstring)
    stop = find(text,'RPMs more than 1 months old')
    msg = text[start+len(startstring):stop]
    #print msg
    mailmsg = open(mytemp,'w')
    mailmsg.write(msg)
    mailmsg.close()
    os.system('mail mew37@cs.yale.edu -s "RPM Check on ftp2" < %s' % mytemp)
    #clean up
    os.remove(mytemp)

if __name__ == '__main__':
    main()
