
LBITS = $(shell getconf LONG_BIT)
ifeq ($(LBITS),64)
ARCH = elf64
else
ARCH = elf
endif
	
sandbox: sandbox.o
	ld -o sandbox sandbox.o

sandbox.o: sandbox.asm
	nasm -f $(ARCH) -g -F stabs sandbox.asm -l sandbox.lst
clean:
	rm -rf sandbox	*.o *.lst
