;  Executable name : hexdump2
;  Version         : 1.0
;  Created date    : 4/15/2009
;  Last update     : 4/20/2009
;  Author          : Jeff Duntemann
;  Description     : A simple hex dump utility demonstrating the use of
;                    assembly language procedures
;
;  Build using these commands:
;    nasm -f elf -g -F stabs hexdump2.asm
;    ld -o hexdump2 hexdump2.o
;

SECTION .bss 					;section containing uninitialized data
	BUFFLEN EQU 10
	Buff resb BUFFLEN

SECTION .data					;section containing initialized data

; Here we have two parts of a single useful data structure, implementing
; the text line of a hex dump utility. The first part displays 16 bytes in
; hex separated by spaces. Immediately following is a 16-character line
; delimited by vertical bar characters. Because they are adjacent, the two
; parts can be referenced separately or as a single contiguous unit.
; Remember that if DumpLin is to be used separately, you must append an
; EOL before sending it to the Linux console.

DumpLin: db " 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 "
DUMPLEN  EQU $-DumpLin
ASCLin:  db "|................|",10
ASCLEN   EQU $-ASCLin
FULLLEN  EQU $-DumpLin

; The HexDigits table is used to convert numeric values to their hex
; equivalents. Index by nybble without a scale: [HexDigits+eax]

HexDigits: db "0123456789ABCDEF"

; This table is used for ASCII character translation, into the ASCII
; portion of the hex dump line, via XLAT or ordinary memory lookup.
; All printable characters "play through" as themselves. The high 128
; characters are translated to ASCII period (2Eh). The non-printable
; characters in the low 128 are also translated to ASCII period, as is
; char 127.
DotXlat:
       db 2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh
       db 2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh
       db 20h,21h,22h,23h,24h,25h,26h,27h,28h,29h,2Ah,2Bh,2Ch,2Dh,2Eh,2Fh
       db 30h,31h,32h,33h,34h,35h,36h,37h,38h,39h,3Ah,3Bh,3Ch,3Dh,3Eh,3Fh
       db 40h,41h,42h,43h,44h,45h,46h,47h,48h,49h,4Ah,4Bh,4Ch,4Dh,4Eh,4Fh
       db 50h,51h,52h,53h,54h,55h,56h,57h,58h,59h,5Ah,5Bh,5Ch,5Dh,5Eh,5Fh
       db 60h,61h,62h,63h,64h,65h,66h,67h,68h,69h,6Ah,6Bh,6Ch,6Dh,6Eh,6Fh
       db 70h,71h,72h,73h,74h,75h,76h,77h,78h,79h,7Ah,7Bh,7Ch,7Dh,7Eh,2Eh
       db 2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh
       db 2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh
       db 2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh
       db 2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh
       db 2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh
       db 2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh
       db 2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh
       db 2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh,2Eh

SECTION .text          ; Section containing code

;-------------------------------------------------------------------------
; ClearLine: Clear a hex dump line string to 16 0 values
; UPDATED:  4/15/2009
; IN:       Nothing
; RETURNS:  Nothing
; MODIFIES: Nothing
; CALLS:    DumpChar
; DESCRIPTION: The hex dump line string is cleared to binary 0 by
;              calling DumpChar 16 times, passing it 0 each time.

ClearLine:
		pushad			; Save all callers GP registers
		mov edx,15		; We're going to go 16 pokes, counting from 0
.poke: 	mov eax,0		; Tell Dumpchar to poke a '0'
		call DumpChar	; Instert the '0' into the hex dump string
		sub edx,1		; Decrement edx , doesn't affect CF!
		jae .poke		; Loop back if edx >= 0
		popad			; restore the caller's GP registers
		ret				; go home
		
;-------------------------------------------------------------------------
; DumpChar:    "Poke" a value into the hex dump line string.
; UPDATED:     4/15/2009
; IN:          Pass the 8-bit value to be poked in EAX.
;              Pass the value's position in the line (0-15) in EDX
; RETURNS:     Nothing
; MODIFIES:    EAX, ASCLin, DumpLin
; CALLS:       Nothing
; DESCRIPTION: The value passed in EAX will be put in both the hex dump
;              portion and in the ASCII portion, at the position passed
;              in EDX, represented by a space where it is not a
;              printable character.

DumpChar:
		push ebx		; save caller's ebx
		push edi		; save caller's edi
; First we insert the input char into the ASCII portion of the dump line
		mov bl,byte [DotXlat+eax]	; translate non-printables to '.'
		mov byte [ASCLin+edx+1],bl  ; write to ASCII portion
