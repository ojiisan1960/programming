/* C by Discover
 * Learning Activity 19
 * page 206
 *
 * The output of this program should be
 *
 * 	y is 4, x is 5, and z is 7
 * 	y is 4, x is 7, and z is 5.
 *
 */

#include <stdio.h>

/* function declaration */
/* fill in the declaration of switchx()
 */
void switchx( .... );

void main( void )
{
	int x, y, z, *int_ptr;

	x = 5;
	y = 4;
	z = 7;
	int_ptr = &x;
	
	printf("\n\n";
	printf(" y is %d, x is %d, and z is %d\n", y, x, z );

	/* call switchx */
	switchx( ..... );
	
	printf(" y is %d, x is %d, and z is %d\n", y, x, z );
}

/* function switchx */
	void switchx( ..... )
	{
	/* fill in the values needed to switch x and z */

	}



