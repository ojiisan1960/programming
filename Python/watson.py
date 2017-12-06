#!/usr/bin/env python2
#
# watson.py - A tool to query the irm database
#
#

import MySQLdb
import sys

if not len(sys.argv) == 3:
    print "Usage: %s [room|name|contact|net-port] <query>" % sys.argv[0]
    sys.exit(0)
 
# Connect to zelda
db=MySQLdb.connect(host="zelda.cs.yale.edu",passwd="hunterkun",db="irm")

# Make a command object
com=db.cursor()

#run a query
com.execute("""SELECT room,name,contact,net_port FROM computers WHERE %s like '%s' order by '%s'""" % (sys.argv[1],sys.argv[2],sys.argv[2]))

data=com.fetchall()

#all done
db.close()

# now display it
print "Room\tName\tUser/Owner\tNet Port"
count = 0   # I can ignore the first one
while (count < len(data)):
    print "%s\t%s\t%s\t%s" % data[count]
    count = count + 1
