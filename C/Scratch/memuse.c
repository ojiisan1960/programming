/********************************************* 
 * memuse.c - try and use more memory than limit
 *  allows.
 *
 *********************************************/ 

#include <stdlib.h>
#include <stdio.h>

#define ONE_MEG (1024 * 1024)

int main()
{
	char *some_mem;

	some_mem = (char *)malloc((ONE_MEG * 2));
	if (some_mem == NULL) exit(EXIT_FAILURE);
	sprintf(some_mem,"Blah blah blah\n");
	printf("%s", some_mem);
	exit(EXIT_SUCCESS);
}

