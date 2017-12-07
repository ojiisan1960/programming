/*
 * Demonstrates the extended ASCII character set
 * 
 */

#include <stdio.h>

unsigned char x;

int main()
{
  /* Print extended ASCII character set */
  for (x = 180; x < 204; x++)
  {
    printf("\nASCII code %d is character %c", x, x);
  }
    printf("\n");
}
