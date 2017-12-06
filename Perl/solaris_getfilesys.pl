#!/usr/local/bin/perl
#
# this will get a list of filesystems that should be backed up
# on a linux box

open (FSTAB, "/etc/vfstab") ||
        die ("Cannot open /etc/vfstab");

        $line = <FSTAB>;
        while ($line ne "" ){
                @filesys = grep (/ufs/ && ! /\#/ && ! /floppy/,$line);
                foreach $filesys (@filesys){
                    @devfile = split (/\s+/,$filesys);
                    print ("Backing up $devfile[0] last mounted on $devfile[2]\n");
                    }
                $line = <FSTAB>;
        }


