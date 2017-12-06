/* The MagPi Issue 3 
 Challenge question 
 This will not compile as is
 There are 4 errors
*/

#include <stdio.h>
int main()
{
    int i = 100, j = 9, k;
    i = i/10;
    k = i - j;
    printf("Well done this program compiles.\n");
    printf("%d - %d = %d\n",i,j,k);
    return 0;
}
