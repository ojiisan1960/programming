/*********************************************
 * pointerthing.c - shows basic pointer stuff
 *
 */

#include <stdio.h>
int main()
{
	int thing_var;
	int *thing_ptr;

	thing_var = 2; /*give thing_var a value*/

  printf("The lvalue of thing_var is %p\n",&thing_var);
  printf("The lvalue of thing_ptr is %p\n",thing_ptr);
  printf("The rvalue of thing_var is %d\n",thing_var);
  printf("The rvalue of thing_ptr is %d\n",*thing_ptr);
  printf("\n");

	printf("using thing_ptr = &thing_var \n");

	thing_ptr = &thing_var; /* make the pointer point to thing_var*/

  printf("The rvalue of thing_ptr is %p\n",thing_ptr);
  printf("\n");
	printf("using *thing_ptr = 3 \n");

	*thing_ptr = 4; /*assign a new value to thing_var*/

  printf("The rvalue of thing_var is %d\n",thing_var);
  printf("\n");
	return(0);
}



