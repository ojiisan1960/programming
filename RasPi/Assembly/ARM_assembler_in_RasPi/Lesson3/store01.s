/* store01.s */

/* ---- Data section ---- */
.data

.balign 4		/* Ensure variable is 4-byte aligned */
myvar1:			/* Define storage for myvar1 */
	.word 0		/* Contents of myvar1 is just 4 bytes */
				/* containing value 3 */

.balign 4		/* Ensure variable is 4-byte aligned */
myvar2:			/* Define storage for myvar2 */
	.word 0		/* Contents of myvar2 is just 4 bytes */
				/* containing value 4 */
	
/* ---- Code section ----*/
.text

.balign 4		/* Ensure code is 4-byte aligned */

.global main

main:
	ldr r1, addr_of_myvar1	/* load the address of myvar1 */
	mov r3, #3				/* the value 3 -> r3  */
	str r3, [r1]			/* r3 -> r1  */
	ldr r2, addr_of_myvar2  /* load the address of myvar2 */
	mov r3, #4				/* the value 4 -> r3  */
	str	r3, [r2]			/* r3 -> r2 */
	add r0,r1,r2
	bx lr

/*---- Labels needed to access Data ----*/

addr_of_myvar1	:	.word myvar1
addr_of_myvar2	:	.word myvar2
