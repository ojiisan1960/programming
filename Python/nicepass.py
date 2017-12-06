#!/usr/bin/env python
#
# Make a semi readable password from the /usr/share/dict/linux.words file
# 
import random
import string

# Ask user how many passwords
print 'How many do you want? :',
num = raw_input()
num = string.atoi(num)

#words = open('/usr/share/dict/linux.words')
words = open('/var/lib/dict/words')

# Make a list
biglist = words.readlines()
 
words.close()

# make two more lists start with empty lists
firstthree = []
lastthree = []

for word in biglist:
	firstthree.append(word[:3])
	lastthree.append(word[-4:-1])

# Now print some
for p in range(num):
	print "%s%s%d" % (lastthree[random.randrange(len(lastthree))] ,
    firstthree[random.randrange(len(firstthree))] , random.randrange(100) )
