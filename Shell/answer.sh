#!/bin/bash




echo "Continue? y|n"
read ANS
case $ANS in
	y)
	echo continue
	;;
	n)
	echo stop
esac
