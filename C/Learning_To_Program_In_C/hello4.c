
#include <unistd.h>
#define STDOUT 1
#define MESSAGE "Hello World\n"
#define SIZE 13

void main()
{
  write(STDOUT, MESSAGE, SIZE);
}
