#!/bin/bash
# read a file with the first column as numbers and get a total
$total=0

for i in `cat $1 | awk '{print $1}'` 
do 
    echo $i
    total=$(( total + $i )) 
done

echo $total
