/* asst2 - print assigned values in different formats
 *
 */

#include<stdio.h>

void main()
{
  char c;
  short i;

  c = 'A';
  i = 65;

  printf("c: dec=%d oct=%o hex=%x ASSCI=%c\n",
      c, c, c, c);
  printf("i: dec=%d oct=%o hex=%x unsigned=%u\n",
      i, i, i, i);

  c = 'X';
  i = -4;

  printf("c: dec=%d oct=%o hex=%x ASSCI=%c\n",
      c, c, c, c);
  printf("i: dec=%d oct=%o hex=%x unsigned=%u\n",
      i, i, i, i);
}
