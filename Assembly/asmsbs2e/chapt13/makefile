sandbox: sandbox.o
	gcc -o sandbox sandbox.o

sandbox.o: sandbox.asm
	nasm -f elf -g -F stabs sandbox.asm -l sandbox.lst
clean:
	rm -rf sandbox	*.o *.lst
