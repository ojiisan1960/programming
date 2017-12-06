/* prog6a - simple 32 bit addition */

.global _start

_start:
	mov r1, #50			/* put 50 into R1 */
	mov r2, #60			/* put 60 into R2 */
	ADDS r0, r1, r2		/* 50 + 60 -> R0 */

	mov r7, #1			/* syscall exit */
	swi 0
