
#include <stdio.h>

int main()
{
    int foo = 10;
    int bar = 50;
    int baz;

    baz = (foo < bar ) ? foo : bar;

    printf("baz = %d\n", baz);

    return 0;
}
