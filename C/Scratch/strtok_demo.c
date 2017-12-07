/*
 www.tutorialspoint.com
*/

#include <string.h>
#include <stdio.h>

int main () {
//   char str[80] = "This is - www.tutorialspoint.com - website";
   char str[ ] = "70.1,95,15:00";
   const char s[2] = ",";
   char *token;
   
   /* get the first token */
   token = strtok(str, s);
   
   /* walk through other tokens */
   while( token != NULL ) {
      printf( " %s\n", token );
    
      token = strtok(NULL, s);
   }
   
   return(0);
}
