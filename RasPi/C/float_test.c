/* The MagPi Issue 4 */

#include <stdio.h>
int main()
{
float f = 3.14159;      /* Assign the approximate value of PI. */
printf("%f\n",f);       /* Print the value stored in f. */
printf("Adding 0.0000001 to %f\n",f);
f+=0.0000001;           /* Add a very small number to it. */
printf("%f\n",f);       /* Print the value stored in f. */
return 0;               /* Return success to the operating system */
}
