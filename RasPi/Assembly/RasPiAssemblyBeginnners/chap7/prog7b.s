/* prog7b - using syscall to read in a string
 * syscall register parameters
 * R0 - file descriptor
 * R1 - the address of the buffer for the string
 * R2 - length of the 
 * R7 - syscall code
 */

.global _start

_start:

_read:
	mov r7, #3			/* syscall read from a file descriptor */
	mov r0, #0			/* stdin file descriptor */
	mov r2, #5			/* read first 5 chars */
	ldr r1,=string
	swi 0

_write:
	mov r7, #4			/* syscall write to file descriptor */
	mov r0, #1			/* stdout file descriptor */
	mov r2, #19			/* string length */
	ldr r1,=string		/* string address */
	swi 0

_exit:
	mov r7, #1			/* syscall exit */
	swi 0

.data					/* data section */

string:
.ascii "Hello World String\n"
