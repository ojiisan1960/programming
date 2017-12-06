#!/usr/bin/env python
#
# Reading a file and looking for something
#myfile = open('file').readlines()
#for line in myfile:
#     line = line[:-1] # strip newline char
#     if re.compile('@').search(line):
#             print line


def FirstCleaning(infile):
    """Get rid of mailman aliases and local aliases"""
    import string
    myfile = open(infile).read()
    start = string.find(myfile,'# Person Aliases')
    stop = string.find(myfile,'Lastnames => database names')

    outfile = open('trimmed','w')

    outfile.write(myfile[start:stop])

    outfile.close()
    return

def MailAddressOnly(infile):
    """Get only lines with something@somewhere"""
    import re
    f1 = open(infile, "r")
    f2 = open('a2', "w")
    while 1:
        text = f1.readline()
        if text == "":
            break
        if re.compile('@').search(text):
            f2.write(text)
    f1.close()
    f2.close()
    return

def PostmasterOnly(infile):
    """Get only the postmast aliases"""
    import re
    f1 = open(infile, "r")
    f2 = open('postmaster', "w")
    while 1:
        text = f1.readline()
        if text == "":
            break
        if re.compile('postmaster').search(text):
            f2.write(text)
    f1.close()
    f2.close()
    return

def CSOnly(infile):
    """Get only the CS aliases """
    import re
    f1 = open(infile, "r")
    f2 = open('cs-mail-addresses', "w")
    while 1:
        text = f1.readline()
        if text == "":
            break
	if re.compile('postmaster').search(text):
	    continue
        if re.compile('@cs.yale.edu').search(text):
            f2.write(text)
    f1.close()
    f2.close()
    return

def NonYaleOnly(infile):
    """Get non Yale mail addresses"""
    import re
    f1 = open(infile, "r")
    f2 = open('non-yale', "w")
    while 1:
        text = f1.readline()
        if text == "":
            break
        if re.compile('yale|netra|spencer|minerva|@james',re.I).search(text):
	    continue
        f2.write(text)
    f1.close()
    f2.close()
    return

if __name__ == '__main__':

    FirstCleaning('aliases')
    MailAddressOnly('trimmed')
    #PostmasterOnly('a2')
    CSOnly('a2')
    NonYaleOnly('a2')
