/* A simple assembly program */

.global _start

_start:
	mov r1, #0xF000000F
	movs r0, r1, ROR #3
	ldr r0,=string

_write:
	mov r7, #4			/* syscall - write to file descriptor */
	mov r0,	#1			/* stdout file descriptor */
	mov r2, #1			/* one character */
	ldr r1,	=string		/* start of string */
	swi 0

_exit:
	mov r7, #1			/* syscall - exit */
	swi 0

.data

	string:	.ascii " "

