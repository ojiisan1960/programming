
#include <stdio.h>

int main(){
  char foo = 'A'; /* foo rvalue is the ascii code for A */
  char bar[] = "A"; /* char array string A */

  printf("foo: %d\n", foo);
  printf("bar: %s\n", bar);

}
