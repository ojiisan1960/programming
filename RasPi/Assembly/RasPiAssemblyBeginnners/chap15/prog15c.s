/**** Use post-indexed addrs to concat strings ****/
/*												  */

.global _start

_start:
	LDR R2, =string1	@ address of both strings
	LDR R3, =string2

_loop:
	LDRB R0, [R3], #1	@ get string2 byte & +1
	CMP R0, #0			@ end of string?
	BNE _loop			@ no, then get the next byte
	SUB R3, R3, #1		@ yes, decrement

_copyloop:
	LDRB R0, [R2], #1	@ get byte from string1
	STRB R0, [R3], #1	@ add to end of string2
	CMP R0, #0			@ end of string?
	BNE _copyloop		@ if not get the next char

_write:
	MOV R0, #1			@ write to stdout
	LDR R1, =string2
	MOV R2, #24
	MOV R7, #4			@sys_write
	SWI 0				@ call sys_write

_exit:
	MOV R7, #1			@sys_exit
	SWI 0				@call sys_exit

.data

string1:
    .asciz "ABCDEFGHIJKL"	@ asciz adds a NULL char at the
							@ end of a string
string2:
    .asciz "012345678910"

padding:
    .ascii "            "
