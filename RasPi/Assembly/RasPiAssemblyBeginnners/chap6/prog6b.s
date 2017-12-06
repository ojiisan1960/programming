/* prog6b - add two 64 bit numbers */

.global _start

_start:
	mov r2, #0xffffffff		/* low half of first number */
	mov r3, #0x1			/* high half of first number */
	mov r4, #0xffffffff		/* low half of second number */
	mov r5, #0xff			/* high half of second number */
	adds	r0,r2,r4		/* add low halves set flag */
	adc	r1,r3,r5			/* add high with carry */

	mov r7,  #1				/* syscall exit */
	swi 0
