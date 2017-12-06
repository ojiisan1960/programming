#!/bin/bash
#
# Read a list of Netids and pull out the full name

for i in `cat foo` 
do 
echo -n $i
ldapsearch -x -H ldap://directory.yale.edu/ -b o=yale.edu uid=$i cn | grep cn: 
done | sed -e 's/cn:/ /g'
