/*
 * From Teach Yourself C in 21 Days
 * Chap 10 
 * Listing 10.1
 * Demonstration of the numeric nature of type char variables
 */

#include <stdio.h>

/* Declare and initilize two char variables */

char c1 = 'a';
char c2 = 90;

int main()
{
  /* Print variable c1 as a char and then as a number */
  printf("\nAs a character, variable c1 is %c", c1);
  printf("\nAs a number, variable c1 is %d", c1);
  /* Do the same for variable c2 */

  printf("\nAs a character, variable c2 is %c", c2);
  printf("\nAs a number, variable c2 is %d\n", c2);
}

