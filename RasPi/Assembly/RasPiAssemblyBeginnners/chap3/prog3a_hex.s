
/* A simple assembly program */

.global _start

_start:
	mov r0, #0x20		/* decimal 32 */
	mov r7, #1	
	swi 0
