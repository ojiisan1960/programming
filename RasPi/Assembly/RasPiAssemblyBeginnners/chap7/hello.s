/* Print a string a number of times */

.global _start

_start:

	mov	r5, #5			/* number of iterations */
_write:
	mov r7, #4			/* syscall write to file descriptor */
	mov r0, #1			/* stdout file descriptor */
	mov r2, #19			/* string length */
	ldr r1,=string		/* string address */
	swi 0				/* print the string */
	subs r5, r5, #1
	bne _write

_exit:
	mov r7, #1			/* syscall exit */
	swi 0

.data					/* data section */

string:
.ascii "Hello World String\n"
