#!/usr/bin/env python2

import MySQLdb

# Connect to zelda
db=MySQLdb.connect(host="zelda.cs.yale.edu",passwd="hunterkun",db="keystone")

# Get a command object
com=db.cursor()

#run a command
com.execute("""SELECT sid,num_follows,problem FROM slips WHERE currtech='mew37' AND  status='O'""")

data=com.fetchall()

#all done
db.close()

# now display it

count = 1   # I can ignore the first one
while (count < len(data)):
    print "PID= %s FO= %s Prob= %s" % data[count]
    count = count + 1
