/* prog7a - using syscall to output a string
 * syscall register parameters
 * R0 - output stream
 * R1 - the address of the string
 * R2 - length of the string
 * R7 - syscall code
 */

.global _start

_start:
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
