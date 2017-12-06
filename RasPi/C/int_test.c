/* The MagPi Issue 4
 * 
 */

#include <stdio.h>
int main()
{
  int i = 2147483647;   /* Assign (2^31)-1 to i */
  printf("%d\n",i);
  printf("Adding 1 to %d\n",i);
  i++;                  /* Increment i by one */
  printf("%d\n",i);     /* Print the value of i */
  return 0;             /* Return success to the operating system. */
}
