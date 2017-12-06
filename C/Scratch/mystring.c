/*
 * mystring.c
 *
 */


#include <stdio.h>

int main(int argc, char **argv)
{
  char mystring[ ] = "aaa,bbb,ccc";
  int index;
	
  while( index < sizeof(mystring)){
   printf("%d",mystring[index]);
   if ( mystring[index] == 44 ){
   printf("\n");
   }
    index++;
  }

  printf("\n");

	return 0;
}
