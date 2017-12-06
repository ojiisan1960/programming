#!/usr/bin/env python
#script for writing a shakespearean insult to the .signature file. special thanks
#to Chris Seidel for making the Shakespearean Insult page.
#I originally wrote this in perl and the script is entirely unreadable to me now.
#My server just got completely rebuilt and now all of the perl libraries are missing;
#so, insead of hunting them down, I decided to rewrite the thing in python.
#I am sure this can be improved upon, if you have any comments please feel free to
#email me at kauphlyn@speakeasy.org. 
 
import urllib
import re
def getinsult():
#get the html file and write it to .tpm.txt
	urllib.urlretrieve('http://www.pangloss.com/seidel/Shaker/index.html', '.tmp.txt')
# open .tmp.txt for reading
	f = open('.tmp.txt')
# open .signature for writing
	sig = open('.signature', 'w')
#read from .tmp.txt
	a = f.read()
# close the .tmp.txt file
	f.close()
# Remove html code
	a = re.sub('<([a-z]|[A-Z])+>|</([a-z]|[A-Z])+>','',a)
	a = re.sub('(<.+>)','',a)
	a = re.sub('\\n','',a)
	a = re.sub('Shakespearean Insulter','',a)

	if re.search('Taken from:', a):
		list2 = re.split('Taken from:', a)
		list3 = re.split('Adapted', list2[1])
		sig.write('--------------------------------------------\n')
		sig.write(list2[0]+'\n-William Shakespeare,'+ list3[0])
		sig.close()
	else:
		getinsult()

getinsult()
