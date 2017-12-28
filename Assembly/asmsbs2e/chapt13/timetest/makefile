all: timetest

timetest: timetest.o
	gcc -o timetest timetest.o

timetest.o: timetest.asm
	nasm -f elf -g -F stabs timetest.asm -l timetest.lst
clean:
	rm -rf timetest	*.o *.lst
