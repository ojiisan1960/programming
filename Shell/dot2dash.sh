#!/usr/local/bin/bash
#
# Subsitute digit.digit to digit-digit
# sed 's/\([0-9][0-9]*\)\.\{1,\}\([0-9][0-9]*\)/\1-\2/'

for i in `ls *.pdf`
do
mv $i `echo $i | sed 's/\([0-9][0-9]*\)\.\{1,\}\([0-9][0-9]*\)/\1-\2/'`
done
