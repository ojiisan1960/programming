/* prog8a - using ORR to toggle upper case to lower */

.global _start

_start:

_read:
	mov r7,	#3			/* syscall - read from file descriptor */
	mov r0,	#0			/* stdin file descriptor */
	mov r2,	#1			/* read only one character */
	ldr r1,	=string		/* load R1 with string address */
	swi 0

_togglecase:
	ldr r1,	=string		/* address of character */
	ldr r0,	[r1]		/* load contents of address */
	orr r0,	r0, #0x20	/* toggle case */
	str r0, [r1]		/* write character back to r1 */

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

