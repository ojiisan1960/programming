/* prog8b - convert a number to binary and print to screen */
/* compare to chap8/prog8b */

.global _start

_start:
	mov r6, #105		/* number to convert */
	mov r10, #1			/* set up mask */
	mov r9, r10, lsl #31	/* logical shift left bit in r10 and move to r9 */
	ldr r1, =string		/* address of string */

_bits:
	tst r6, r9			/* test number in r6 with mask in r9 */
	moveq r0, #48		/* ascii '0' */
	movne r0, #49		/* ascii '1' */
	str r0, [r1]
	mov r8, r6
	bl	_write
	mov r6, r8			/* move number ,preserve */
	movs r9, r9, lsr #1	/* shift right 1 for new mask test */
	bne _bits			/* loop until 32 bits are tested */

_newline:				/* add a newline before exit */
	mov r0, #0xA
	str r0, [r1]
	bl _write

_exit:
	mov r7, #1
	swi 0

_write:
	mov r7, #4			/* syscall - write to file descriptor */
	mov r0, #1			/* stdout file descriptor */
	mov r2, #1			/* length of character */
	swi 0
	bx lr				/* break to instruction in lr ? */	
				
.data
	string: .ascii " "

