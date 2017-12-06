#!/usr/bin/env python
#
# Get TV listings 
import urllib,os,tempfile
from string import find

# Make a dictionary of channels and urls
urls = {'sci-fi': 'http://tv.yahoo.com/tvpdb?d=tvs&id=166030932&channels=us_SCIFI&lineup=us_CT06412&.intl=us',
	'disc': 'http://tv.yahoo.com/tvpdb?d=tvs&id=166030932&channels=us_DSC&lineup=us_CT06412&.intl=us',
	'nick':'http://tv.yahoo.com/tvpdb?d=tvs&id=166030932&channels=us_NIK&lineup=us_CT06412&.intl=us',
	'toon':'http://tv.yahoo.com/tvpdb?d=tvs&id=166030932&channels=us_TOON&lineup=us_CT06412&.intl=us',
	'hist':'http://tv.yahoo.com/tvpdb?d=tvs&id=166030932&channels=us_HISTORY&lineup=us_CT06412&.intl=us',
	'amc':'http://tv.yahoo.com/tvpdb?d=tvs&id=166030932&channels=us_AMC&lineup=us_CT06412&.intl=us'
}

def getListings(channel):
    """Get the TV listings and print em"""
    url = urls[channel]
    # make a temp file for the html crud
    mytemp = tempfile.mktemp()
    htmlcrud = open(mytemp,'w')
    htmlcrud.write(urllib.urlopen(url).read())
    # close file
    htmlcrud.close()
    # use lynx to read file 
    text = os.popen('lynx -dump -force_html -nolist -width=200 %s' % mytemp).read() 
    start = find(text,'Program Schedule')
    stop = find(text,'Search')
    print text[start:stop]
    # clean up
    os.remove(mytemp)

if __name__ == '__main__':
    import sys
    if not len(sys.argv) >1:
	print "Usage: %s <station id>" % sys.argv[0]
	for key in urls.keys():
	    print key,
	sys.exit(1)
    getListings(sys.argv[1])
