#!/usr/bin/python2.2
#
# Make a login:password-hash line for a .htpasswd file
#
# created by Mark Wogahn 06/23/03
#
# 
import random
import crypt
import string

loginname = raw_input('Enter login name :')
pw = raw_input('Enter password :')

# grab a random string for crypt salt
words = open('/usr/share/dict/linux.words')
biglist = words.readlines()
words.close()

# make two more lists start with empty lists
lastthree = []
for word in biglist:
        lastthree.append(word[-4:-1])

saltstr = lastthree[random.randrange(len(lastthree))]

hash = crypt.crypt(pw,saltstr)
print 'Cut and past the following line to your .htpassword file:'
print ""
print '%s:%s' % (loginname,hash)
