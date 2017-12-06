#!/usr/bin/env python2

f = open('Download.csv')
count = 0
for line in f.readlines():
     col = string.split(line,',')
     sub = count + string.atof(col[4])
     print "%f + %f = %f" % (string.atof(col[4]),count,sub)
     count = sub
