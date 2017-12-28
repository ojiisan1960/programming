randtest: randtest.o
	gcc -o randtest randtest.o

randtest.o: randtest.asm
	nasm -f elf -g -F stabs randtest.asm -l randtest.lst
clean:
	rm -rf randtest	*.o *.lst
