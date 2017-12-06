/* multiply two numbers with MLA */
/* MLA - multiply with accumulate */
/* R0 = (R1 * R2 ) + R3 */

.global _start

_start:
	mov r1, #20
	mov r2, #5
	mov r3, #10
	mla r0, r1, r2, r3	/* r0 = (r1 * r2 ) + r3 */

	mov r7, #1
	swi 0
