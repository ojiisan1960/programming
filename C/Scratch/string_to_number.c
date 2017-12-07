/*
 * How does atoi() work?
 * From https://www.tutorialspoint.com/c_standard_library/c_function_atoi.htm
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main () {
   int val;
   char str[20];
   
   //strcpy(str, "70.0,95,15:00");
   //strcpy(str, "70.0");
 //  strcpy(str, "95");
   strcpy(str, "15:00");
   val = atoi(str);
   val = val-12;
   printf("String value = %s, Int value = %d\n", str, val);

//   strcpy(str, "tutorialspoint.com");
//   val = atoi(str);
//   printf("String value = %s, Int value = %d\n", str, val);

   return(0);
}
