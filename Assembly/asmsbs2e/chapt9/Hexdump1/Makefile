
LBITS = $(shell getconf LONG_BIT)
ifeq ($(LBITS),64)
ARCH = elf64
else
ARCH = elf
endif
	
hexdump1: hexdump1.o
	ld -o hexdump1 hexdump1.o

hexdump1.o: hexdump1.asm
	nasm -f $(ARCH) -g -F stabs hexdump1.asm -l hexdump1.lst
clean:
	rm -rf hexdump1	*.o *.lst
