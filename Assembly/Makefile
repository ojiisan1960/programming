
LBITS = $(shell getconf LONG_BIT)
ifeq ($(LBITS),64)
ARCH = elf64
else
ARCH = elf
endif
	
hello: hello.o
	ld -o hello hello.o

hello.o: hello.asm
	nasm -f $(ARCH) -g -F stabs hello.asm -l hello.lst
clean:
	rm -rf hello	*.o *.lst
