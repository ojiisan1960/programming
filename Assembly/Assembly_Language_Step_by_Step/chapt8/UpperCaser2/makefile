
LBITS = $(shell getconf LONG_BIT)
ifeq ($(LBITS),64)
ARCH = elf64
else
ARCH = elf
endif
	
uppercaser2: uppercaser2.o
	ld -o uppercaser2 uppercaser2.o

uppercaser2.o: uppercaser2.asm
	nasm -f $(ARCH) -g -F stabs uppercaser2.asm -l uppercaser2.lst
clean:
	rm -rf uppercaser2	*.o *.lst
