
LBITS = $(shell getconf LONG_BIT)
ifeq ($(LBITS),64)
ARCH = elf64
else
ARCH = elf
endif
	
kangroo: kangroo.o
	ld -o kangroo kangroo.o

kangroo.o: kangroo.asm
	nasm -f $(ARCH) -g -F stabs kangroo.asm -l kangroo.lst
clean:
	rm -rf kangroo	*.o *.lst
