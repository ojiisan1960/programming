#!/bin/bash

for i in `cat $1`
do
	#echo "Checking for file $i..."
	ls -l $i > /dev/null 2>&1
	if [ $? -gt 0 ];then
	echo "File $i was not restored"
	fi
done
