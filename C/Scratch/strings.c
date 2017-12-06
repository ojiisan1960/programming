
#include <stdio.h>

int main(){
    char workstring[] = "foo,bar,baz";
    /* print the string */
    printf("%s\n",workstring);
    /* print the lvalue of the string */
    printf("%p\n",&workstring);
    printf("Size of string: %lu\n",sizeof(workstring));
}
