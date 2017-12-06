/* prog8b - convert a number to binary and print to screen */

.global _start

_start:
	mov r6, #15		/* number to convert */
	mov r10, #1			/* set up mask */
	mov r9, r10, lsl #31	/* logical shift left bit in r10 and move to r9 */
	ldr r1, =string		/* address of string */

_bits:
	tst r6, r9			/* test number in r6 with mask in r9 */
	beq _print0			/* test masked bit in number, if exists _print0 */
	mov r8, r6			/* move and preserve number */
	mov r0, #49			/* ascii "1" */
	str r0, [r1]		/* storge 1 in string */
	bl	_write
	mov r6, r8			/* move number ,preserve */
	bal _noprint1

_print0:
	mov r8, r6
	mov r0, #48			/* ascii "0" */
	str r0, [r1]
	bl _write
	mov r6, r8

_noprint1:
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
	mov pc, lr			/* move link reg address to program counter */
						/* continue from after bl _write: in _bits: */
.data
	string: .ascii " "

