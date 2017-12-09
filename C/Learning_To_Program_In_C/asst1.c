#include <unistd.h>

void main()
{
  /* print out 13 characters to stdout */
  write(1, "Hello World!\n",13);
}
