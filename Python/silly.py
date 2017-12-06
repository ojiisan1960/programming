#! /usr/bin/python2

# v0.3 and v0.3.1 by Daniel Mahler (mahler@cyc.com)

# uses functional abstraction and data structures
# to avoid the code repetition of the original version.
# Also this version uses commandline arg instead of prompting
# eg
# python silly.py 123-4567

# documentation from original script:
##################################################
#   SillyPhone v0.1
#   June 21, 2001
# by Manuel F. Lanctot (manolo@sluggy.net)

# I always wanted to know if I could change my phone number into a word. Would it be
# cool to say "My phone? It's 729-LEET" or some stuff like that.
# And it's chick magnet! :-)

# You are completely free to copy/modify/distribute this file. Just keep the above header please (at least # my name).
# If you have any comments or ideas, email me at manolo@sluggy.net
# I am sure there are other (more simple) ways to do this, but this is my first
# Python script ever, so I didn't work a lot on it.
# There must be some ways to do this without that much lines of code, I'll work on it later, when
# my wooby Python skills get better.
#
# If I get good feedbacks (?!), I will rewrite it for all 7 digits, maybe even 8 digits (for other countries like # France)
###################################################



from sys import argv
from string import *

def descartes(set):
    "compute cartesian product"
    if set:
        return [partial + [next]
                for partial in descartes(set[0:-1])
                for next in set[-1]]
    else:
        return [[]]

# keys[i] == the list of chars for digit
keys = [
    ['0'],
    ['1'],
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l'],
    ['m', 'n', 'o'],
    ['p', 'r', 's'],
    ['t', 'u', 'v'],
    ['w', 'x', 'y']
    ]

# main function
def silly(ph):
    ph = str(ph)
    return [ph[0:-4] + join(word,"")
            for word in descartes([keys[int(i)]
                                   for i in ph[-4:]])]

if __name__=='__main__':
    for x in silly(argv[1]):
        print x

