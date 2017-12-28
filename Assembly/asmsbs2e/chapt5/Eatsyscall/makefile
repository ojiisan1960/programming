
LBITS = $(shell getconf LONG_BIT)
ifeq ($(LBITS),64)
ARCH = elf64
else
ARCH = elf
endif
	
eatsyscall: eatsyscall.o
	ld -o eatsyscall eatsyscall.o

eatsyscall.o: eatsyscall.asm
	nasm -f $(ARCH) -g -F stabs eatsyscall.asm -l eatsyscall.lst
clean:
	rm -rf eatsyscall	*.o *.lst
