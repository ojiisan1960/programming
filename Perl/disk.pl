#!/usr/local/bin/perl
#
@users= `ls /export/home > /tmp/list`;
foreach $users (@users) {
	print ("$users\n");
	print ("\n");

