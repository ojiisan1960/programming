#!/usr/bin/env python
#
# Get Zippy comic

import urllib

url = 'http://www.sfgate.com/cgi-bin/article.cgi?file=/comics/Zippy_the_Pinhead.dtl'
data = urllib.urlopen(url).read()
f = open('pinhead','w')
f.write(data)
f.close()

