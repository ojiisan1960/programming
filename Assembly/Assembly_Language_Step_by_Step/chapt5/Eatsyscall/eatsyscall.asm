;  Executable name : EATSYSCALL
;  Version         : 1.0
;  Created date    : 1/7/2009
;  Last update     : 1/7/2009
;  Author          : Jeff Duntemann
;  Description     : A simple assembly app for Linux, using NASM 2.05,
;                    demonstrating the use of Linux INT 80H syscalls
;                    to display text.
;
;  Build using these commands:
;    nasm -f elf -g -F stabs eatsyscall.asm
;    ld -o eatsyscall eatsyscall.o
;
SECTION .data       ; Section containing initialized data

EatMsg: db "Eat at Joe's!", 10
EatLen: equ $-EatMsg

SECTION .bss        ; Section containing uninitialized data

SECTION .text       ; Section containing code

global _start       ; the linker need this to find the entry point

_start:
        nop             ; this nop keeps gdb happy
        mov eax,4       ; syscall for write
        mov ebx,1       ; stdout file descriptor
        mov ecx,EatMsg  ; pass the offset of the message string
        mov edx,EatLen  ; pass the length of the message string
        int 80H         ; syscal to output the message

        mov eax,1       ; syscall for exit
        mov ebx,0       ; exit with return code 0
        int 80H         ; syscall exit 