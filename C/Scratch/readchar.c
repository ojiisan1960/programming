/********************************************* 
 *  a small program to read input from the keyboard
 *  and then echo it again
 **********************************************/ 

#include <stdio.h>

int main()
{
    /* create an array variable to hold at most 256 chars */

    char input[256];

    /* Prompt for a string */

    printf("Enter a string of characters: ");

    /* the scanf function reads from keyboard input */
    /* and 'puts' it the the input array until it sees a newline */

    scanf("%[^\n]",&input);

    /* Then read from the input variable and display it */

    printf("You entered: %s\n", input);

}
    
