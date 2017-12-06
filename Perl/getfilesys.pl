#!/usr/bin/perl
#
# read /etc/fstab and get only what we should backup

open (FSTAB, "/etc/fstab") ||
        die ("Cannot open /etc/fstab");

        $line = <FSTAB>;
        while ($line = <FSTAB>){
                @filesys = grep (/ext/ && !/^#/ && ! /floppy/, $line);
                foreach $filesys (@filesys){
                        @devfile = split (/\s+/,$filesys);
                        print ("$devfile[0] is a filesystem we should backup\n");
                        }
        }
