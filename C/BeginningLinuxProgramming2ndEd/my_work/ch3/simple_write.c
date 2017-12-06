#include <unistd.h>
#include <stdio.h>

int main()
{
    if((write(1,"This is some data\n", 18)) !=18)
	write(2,"A write error has occured on file descriptor 1\n",46);
    exit(0);
}
