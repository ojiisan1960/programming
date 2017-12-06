#!/usr/bin/perl -w
#
#
# Open /etc/passwd and read it
open(P,"</etc/passwd") || die "$0: can't open passwd file, $!\n";

# Read /etc/passwd and split the lines by :
while(<P>)
{

#Cut off newline chars
chomp;


my ($user,$passwd,$uid,$gid,$info,$home,$shell) = split /:/;

print <<EOF;
User:           $user
Password:       Secret
User ID:        $uid
Group ID:       $gid
User Info:      $info
Home Directory  $home
Shell:          $shell

EOF

}

#Close the file handle P
close(P) || die "$0: couldn't close the passwd file, $!\n";
