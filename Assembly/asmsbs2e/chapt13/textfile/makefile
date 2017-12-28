all: textfile

textfile: textfile.o linlib.o
	gcc -o textfile textfile.o linlib.o

textfile.o: textfile.asm 
	nasm -f elf -g -F stabs textfile.asm -l textfile.lst
linlib.o: linlib.asm 
	nasm -f elf -g -F stabs linlib.asm -l linlib.lst
clean:
	rm -rf textfile	*.o *.lst
