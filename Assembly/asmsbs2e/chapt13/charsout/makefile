charsout: charsout.o
	gcc -o charsout charsout.o

charsout.o: charsout.asm
	nasm -f elf -g -F stabs charsout.asm -l charsout.lst
clean:
	rm -rf charsout	*.o *.lst
