#!/usr/bin/env python2
#
import re,os

afile = open('aliases')

def isList(alias):
    """check to see if it is a maillist"""

def cleanAlias(line):
    """take the line and return the alias
       as first last"""
    alias = line[:-1]
    alias = alias.replace('-',' ')
    alias = alias.replace('.',' ')
    alias = alias.split()
    if len(alias) > 1:
	 fullname = '%s %s' % ( alias[1],alias[0] )
	 return fullname

def deadWood(name):
    """user name is not in ph"""
    outfile = open('501','a')
    outfile.write('No match for %s %s' % (name,line))
    print 'No match for %s %s' % (name,line[:-1])
    outfile.close()

def stillHere(result,name,line):
    """We get something from ph"""
    outfile = open('validuser','a')
    outfile.write('%s %s %s' % (name,result,line))
    print '%s %s %s' % (name,result,line[:-1])
    outfile.close()
    

def checkName(name):
    """use ph to check user name"""
    res = os.popen('ph %s' % name).readlines()
    for checkline in res:
	if checkline.find('501') >= 0:
	    deadWood(name)
	else:
	    if checkline.find('email') >= 0:
		#print name,checkline,line
		stillHere(checkline[:-1],name,line)


if __name__ == '__main__':
    #checkName('mark wogahn')

    for line in afile.readlines():
	if re.compile('minerva').search(line):
	    nline = line.split()
	    name = cleanAlias(nline[0])
	    checkName(name)
    os.rename('501','Deadwood')
    os.rename('validuser','CheckedOK')
