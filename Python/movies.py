#!/usr/bin/env python
#
# Get movie listings 
import urllib,os,tempfile
from string import find

url = 'http://movies.yahoo.com/showtimes/showtimes.html?z=06405&m=&t=&a=&r=adv&Submit+Info=Showtimes'


# make a temp file for the html crud
mytemp = tempfile.mktemp()
htmlcrud = open(mytemp,'w')
htmlcrud.write(urllib.urlopen(url).read())
# close file
htmlcrud.close()
# use lynx to read file 
text = os.popen('lynx -dump -force_html -nolist -width=200 %s' % mytemp).read() 
start = find(text,'clicking')
stop = find(text,'Legend')
print text[start+30:stop-16]
# clean up
os.remove(mytemp)

