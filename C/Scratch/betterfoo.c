/********************************************* 
 *  a small program to read input from the keyboard
 *  and then echo it again using fgets and puts 
 *  which are preffered for string handling in C
 *
 *********************************************/ 

#include <stdio.h>

int main()
{
    /* create an array variable to hold at most 20 chars */

    char input[20];

    /* Prompt for a string */

    printf("Enter a string: ");
    
    /* fgets to read from sdtin */

    fgets(input,sizeof(input),stdin);

    /* Then read from the input variable and display it */

    printf("You entered: ");
    puts(input);

}
    
