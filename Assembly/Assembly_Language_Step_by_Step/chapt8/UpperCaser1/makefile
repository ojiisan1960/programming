
uppercaser1: uppercaser1.o
	ld -o uppercaser1 uppercaser1.o
uppercaser1.o: uppercaser1.asm
	nasm -f elf64 -g -F stabs uppercaser1.asm -l uppercaser1.lst

clean:
	rm -rf uppercaser1 *.o *.lst
