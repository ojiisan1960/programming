#! /usr/bin/perl
# 
# Regression test for the 'fort77' driver script.
#

#
# List of tests to run and of expected files.
# 

$test = [
    [ "./fort77 -c foo.f",                 qw(foo.o) ],
    [ "./fort77 -c bar.F",                 qw(bar.o) ],
    [ "./fort77 -c -o gargle.o foo.f",	   qw(gargle.o) ],
    [ "./fort77 foo.f",			   qw(a.out) ],
    [ "./fort77 baz/bazfoo.f",		   qw(a.out) ],
    [ "./fort77 -c baz/bazfoo.f",	   qw(bazfoo.o) ],
    [ "./fort77 -o bar.o -c baz/bazfoo.f", qw(bar.o) ],
    [ "./fort77 -o tscht foo.f",	   qw(tscht) ],
    [ "./fort77 -k foo.f",		   qw(a.out foo.c) ],
    [ "./fort77 -g -k foo.f",		   qw(foo.c a.out) ],
    [ "./fort77 -c -f long.f",		   qw(long.o) ],
    [ "./fort77 mainmiss.f"				],
    [ "./fort77 -c foo.f && ./fort77 -c mainmiss.f && ./fort77 -o foo foo.o mainmiss.o",
           qw(foo.o mainmiss.o foo) ],
    [ "./fort77 -c foo.f && ./fort77 -o foo foo.o mainmiss.f",
	   qw(foo.o foo) ],
    [ "./fort77 synerr.f && touch gargle"		]
];

#
# These files could possibly be generated by a buggy fort77
# script; they are also checked.
#

@unexpected = qw(gargle.c baz/bazfoo.c baz/bazfoo.o mainmiss.o mainmiss.c
		 synerr.o synerr.c baz/a.out bar.c);

foreach $ref (@$test) {
    foreach $file(@$ref[1..@$ref-1]) {
	$files{$file} ++;
    }
}

foreach $file(@unexpected) {
    $files{$file} ++;
}

while ($_ = @ARGV[0]) {
    shift;
    if (/^-v/) {
	$verbose ++;
    }
}

foreach (keys %files) {
    unlink $_;
}

$errors = 0;
foreach $ref (@$test) {

    $cmd = shift(@$ref);
    %expect = ();
    $cmd_error = 0;

    foreach $r (@$ref) {
	$expect{$r} ++;
    }

    print STDERR "$cmd ..." if $verbose > 0;
    $cmd = "( $cmd ) >/dev/null 2>&1" if $verbose <= 1;

    system($cmd);

    foreach (keys %files) {
	-f $_;
	if ($expect{$_}) {
	    if (-f) {
		print STDERR " \"$_\" ok " if $verbose > 2;
	    }
	    else {
		print STDERR "\"$_\" not generated by \"$cmd\"\n";
		$errors ++;
		$error_seen ++;
	    }
	}
	else {
	    if (-f) {
		print STDERR " \"$_\" should not be generated by \"$cmd\"\n";
		$errors ++;
		$error_seen ++;
	    }
	    else {
		print STDERR " \"$_\" n-ok " if $verbose > 3;
	    }
	}
	if (-f) {
	    unlink $_ or die ("Could not unlink $_: $!\n");
        }
    }
    print STDERR " test successful.\n" if $verbose && ! $error_seen;
}

if ($errors == 0) {
    print STDERR "Passed all tests.\n" if $verbose;
    exit 0;
}
else {
    print STDERR "Total $errors error(s) encountered.\n";
    exit 1;
}
