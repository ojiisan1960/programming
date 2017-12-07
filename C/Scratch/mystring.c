/*
 * mystring.c
 *
 */


#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
  char mystring[ ] = "70.0,95,15:00";
  int index;
	
  printf("length of mystring: %d\n",strlen(mystring));
  while( index < strlen(mystring)){
   printf("%d",mystring[index]);
   if ( mystring[index] == 44 ){
   //printf("\n");
   }
   index++;
  }
   printf("\n");

	return 0;
}
