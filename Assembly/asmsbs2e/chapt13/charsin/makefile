charsin: charsin.o
	gcc -o charsin charsin.o

charsin.o: charsin.asm
	nasm -f elf -g -F stabs charsin.asm -l charsin.lst
clean:
	rm -rf charsin	*.o *.lst
