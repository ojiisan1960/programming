;  Executable name : hexdump1
;  Version         : 1.0
;  Created date    : 4/4/2009
;  Last update     : 4/4/2009
;  Author          : Jeff Duntemann
;  Description     : A simple program in assembly for Linux, using NASM 2.05,
;    demonstrating the conversion of binary values to hexadecimal strings.
;    It acts as a very simple hex dump utility for files, though without the
;    ASCII equivalent column.
;
;  Run it this way:
;    hexdump1 < (input file)
;
;  Build using these commands:
;    nasm -f elf -g -F stabs hexdump1.asm
;    ld -o hexdump1 hexdump1.o
;
SECTION .bss                    ;uninitilized data section
		BUFFLEN equ 16          ;read 16 bytes at a time
        Buff:   resb BUFFLEN    ; text buffer

SECTION .data                   ;initilized data section

		HexStr: db  "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ",10
		HEXLEN equ $-HexStr
		Digits db "0123456789ABCDEF"

SECTION .text					;code goes here

global _start					;link needs to find this entry point

_start:
		nop						;keeps gdb happy?

;Read a buffer full of text from stdin

Read:
		mov eax,3				;syscall sys_read
		mov ebx,0				;stdin file descriptor
		mov ecx,Buff
		mov edx,BUFFLEN			;number of bytes to read
		int 80h					;call sys_read
		mov ebp,eax				;save number of bytes read 
		cmp eax,0				;if eax = 0, sys_read reached EOF
		je Done					;finished reading file, exit program

;set up the registers to process the buffer

		mov esi,Buff			;address of buffer into esi
		mov edi,HexStr			;address of HexStr into edi
		xor ecx,ecx				;clear line string pointer to 0

;go through the buffer and convert binary to hex

Scan:
		xor eax,eax				;clear eax to 0

;calculate the offset into HexStr, which is the value in ecx X 3
		mov edx,ecx				;copy character counter to edx
		shl edx,1				;multiply pointer by 2 using shift left
		add edx,ecx				;complete the multiplication X 3

;get a character from the buffer and put it in both eax and ebx

		mov al,byte [esi+ecx]	;put a byte from the buffer into al
		mov ebx,eax				;duplicate the byte into bl for second nybble
	
;look up low nybble character and insert into the string

		and al,0Fh				;mask out all but low nybble
		mov al,byte [Digits+eax] ;look up char equivalent of nybble
		mov byte [HexStr+edx+2],al ;write MSB char digit to string
	
;look up high nybble character and insert into string

		shr bl,4				;shift high 4 bits of char into low 4 bits
		mov bl,byte [Digits+ebx] ;look up char equivalent of nybble
		mov byte [HexStr+edx+1],bl ;write MSB char digit to line string

;bump buffer pointer to the next char and see if we're done

		inc ecx					;increment line string pointer
		cmp ecx,ebp				;compare to number of chars in buffer
		jna Scan		;jump to Scan if ecx <= number of chars in buffer
	
;write the line of hexadecimal values to stdout
	
		mov eax,4		;syscall sys_write
		mov ebx,1		;stdout file descriptor
		mov ecx,HexStr	;offset of string
		mov edx,HEXLEN	;size of the string
		int 80h			;call sys_write
		jmp Read		;loop back and load the buffer again

;all done
	Done:
		mov eax,1		;syscall sys_exit
		mov ebx,0		;return code of 0
		int 80h			;call sys_exit

