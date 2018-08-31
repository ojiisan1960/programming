#!/bin/bash

#Use awk to search the cloud-list
# -v passes an external variable to awk
# the expression '$0 ~ s' searches for an instance of var s in the line

awk -v s=$1 -F/ '$0 ~ s {print $1":",$(NF-3)"/"$(NF-2)"/"$(NF-1)"/"$NF}' cloud-list
