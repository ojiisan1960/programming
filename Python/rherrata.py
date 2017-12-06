#!/usr/bin/env python
#
# Get Redhat update listings 
import urllib,os,tempfile
from string import find

# Make a dictionary of channels and urls
urls = {'6.2': 'https://rhn.redhat.com/errata/rh62-errata.html',
	'7.1': 'https://rhn.redhat.com/errata/rh71-errata.html',
	'7.2': 'https://rhn.redhat.com/errata/rh72-errata.html',
	'7.3': 'https://rhn.redhat.com/errata/rh73-errata.html',
	'8.0': 'https://rhn.redhat.com/errata/rh8-errata.html'
}

def getListings(version):
    """Get the listings and print em"""
    url = urls[version]
    # make a temp file for the html crud
    mytemp = tempfile.mktemp()
    htmlcrud = open(mytemp,'w')
    htmlcrud.write(urllib.urlopen(url).read())
    # close file
    htmlcrud.close()
    # use lynx to read file 
    text = os.popen('lynx -dump -force_html %s' % mytemp).read() 
    #start = find(text,'Red Hat')
    start = find(text,'Synopsis')
    stop = find(text,'Copyright')
    print text[start:stop]
    # clean up
    os.remove(mytemp)

if __name__ == '__main__':
    import sys
    if not len(sys.argv) >1:
	print "Usage: %s <RH version>" % sys.argv[0]
	for key in urls.keys():
	    print key,
	sys.exit(1)
    getListings(sys.argv[1])
