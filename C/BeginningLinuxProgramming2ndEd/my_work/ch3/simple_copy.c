/*
*  Simple_copy.c
* Reads a file named "infile" character by character and writes
*  a copy to "outfile"
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int c;
    FILE *in, *out;
    
    in = fopen("infile","r");
    out = fopen("outfile","w");

    while((c = fgetc(in)) !=EOF)
	fputc(c,out);

    exit(0);
}
