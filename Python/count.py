#!/usr/bin/env python

#
# Count the number of lines, characters, words, and occurences of each word in a
# file.  A word is delimted by whitespace and punctuation (as defined by the
# builting string.whitespace and string.punctuation variables).
#

import sys
import string
import re

# initialize the counters
linecount = 0
charcount = 0
wordcount = 0
# this is where I will store the total count of each word
words     = { }


# iterate over each line on stdin
for line in sys.stdin.readlines() :
    linecount += 1
    charcount += len( line )

    # remove leading and trailing whitespace
    line = string.strip( line ) 

    # split the string into a list of words
    # a word is delimited by whitespace or punctuation
    for word in re.split(
            "[" + string.whitespace + string.punctuation + "]+" ,
            line ) :

        # make the word lower case
        word = string.lower( word )

        # check to make sure the string is considered a word
        if re.match( "^[" + string.lowercase + "]+$" , word ) :
            wordcount += 1

            # if the word has been found before, increment its count
            # otherwise initialize its count to 1
            if words.has_key( word ) :
                words[ word ] += 1
            else :
                words[ word ] = 1

        
# Now print out the results of the count:
print
print "Number of lines:" , linecount
print "Total word count:" , wordcount
print "Total character count:" , charcount
print

# print each word and its count in sorted order
sorted_word_list = words.keys()
sorted_word_list.sort()

for word in sorted_word_list :
    print word , ":" , words[ word ]

