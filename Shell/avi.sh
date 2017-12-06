#!/bin/bash
#
# 
# Take an input file and substitute all occurances of \cspace with \%cspace
# and write to new file. Exit if no input file specified

if [ $# -eq 0 ];then
    echo Usage: $0 inputfile
    exit 1
fi
sed -e 's/\\cspace/\%\\cspace/' < $1 > $1.out
