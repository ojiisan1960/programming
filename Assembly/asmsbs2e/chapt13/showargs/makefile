all: showargs

showargs: showargs.o
	gcc -o showargs showargs.o

showargs.o: showargs.asm
	nasm -f elf -g -F stabs showargs.asm -l showargs.lst
clean:
	rm -rf showargs	*.o *.lst
