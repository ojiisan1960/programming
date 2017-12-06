
LBITS = $(shell getconf LONG_BIT)
ifeq ($(LBITS),64)
ARCH = elf64
else
ARCH = elf
endif
	
vidbuff1: vidbuff1.o
	ld -o vidbuff1 vidbuff1.o

vidbuff1.o: vidbuff1.asm
	nasm -f $(ARCH) -g -F stabs vidbuff1.asm -l vidbuff1.lst
clean:
	rm -rf vidbuff1	*.o *.lst
