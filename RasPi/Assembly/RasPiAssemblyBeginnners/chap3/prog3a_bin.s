
/* A simple assembly program */

.global _start

_start:
	mov r0, #0b10000		/* decimal 16 */
	mov r7, #1	
	swi 0
