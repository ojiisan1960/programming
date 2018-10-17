/* C by Discovery 
 * Example 4-6
 * pg 202
 */

#include <stdio.h>

void changit( int, int * );

void main ( void )
{
	int x, y, *int_ptr;

	x = 1;
	y = 3;
	int_ptr = &y;

	printf("\n\n");
	printf( "In main before the call to changit. ");
	printf(" x = %d, y = %d, *int_ptr = %d\n", x ,y ,*int_ptr);

	/* call changit */
	changit(x, int_ptr);

	printf( "In main after the call to changit.");
	printf(" x = %d, y = %d, *int_ptr = %d\n", x ,y ,*int_ptr);
	printf("\n\n");
}

/* function changit */

void changit( int x, int *int_ptr)
{
	x += 5;
	*int_ptr  += 5;
	printf( "In changit, x = %d, *int_ptr = %d.\n", x ,*int_ptr);
}
