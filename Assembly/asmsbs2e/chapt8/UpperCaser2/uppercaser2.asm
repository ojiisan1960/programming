;  Executable name : uppercaser2
;  Version         : 1.0
;  Created date    : 3/25/2009
;  Last update     : 3/25/2009
;  Author          : Jeff Duntemann
;  Description     : A simple program in assembly for Linux,using NASM 2.05,
;    demonstrating simple text file I/O (through redirection) for reading an
;    input file to a buffer in blocks, forcing lowercase characters to
;    uppercase, and writing the modified buffer to an output file.
;
;  Run it this way:
;    uppercaser2 > (output file) < (input file)
;
;  Build using these commands:
;    nasm -f elf -g -F stabs uppercaser2.asm
;    ld -o uppercaser2 uppercaser2.o
;
SECTION .bss			;section containing uninitialized data
	BUFFLEN equ 1024	;length of buffer
	Buff:	resb BUFFLEN	;buffer

SECTION .data			;section for initialized data

SECTION .text			;section for code

global _start			;linker entry point

_start:				;start label
	nop			;keeps gdb happy

;Read a buffer from stdin
Read:
	mov eax,3		;syscall sys_read
	mov ebx,0		;stdin file descriptor
	mov ecx,Buff		;address of buffer
	mov edx,BUFFLEN		;number of bytes to read in one pass
	int 80h			;call sys_read to fill the buffer
	mov esi,eax		;copy sys_read return value
	cmp eax,0		;If eax = 0, sys_read reached EOL on file
	je Done			;jump to Done if EOL
; Set up the registers to process the buffer
    mov ecx,esi     ;number of bytes read into ecx
    mov ebp,Buff    ;address of buffer into ebp
    dec ebp         ;adjust count to offset

;Go through the buffer and convert lower case to upper case
Scan:
    cmp byte [ebp+ecx],61   ;compare char to 'a'
    jb Next                 ;if below 'a' not lower case jump to Next
    cmp byte [ebp+ecx],7Ah      ;compare char to 'z'
    ja Next                 ;if above 'z' not lower case jump to Next
                            ; next char should be lower case
    sub byte [ebp+ecx],20h  ;convert to upper case
Next:
    dec ecx                 ;decrement counter
    jnz Scan                ; if not 0 return to Scan more chars

;Write the processed buffer to stdout
Write:
    mov eax,4       ;syscall sys_write
    mov ebx,1       ;stdout file descriptor
    mov ecx,Buff    ;address of buffer
    mov edx,esi     ;number of bytes in the buffer
    int 80h         ;call sys_write
    jmp Read        ;jump back to read to fill the buffer

;File is read, program complete
Done:
    mov eax,1       ;syscall sys_exit
    mov ebx,0       ;return code of 0
    int 80h         ;call sys_exit and exit the program
