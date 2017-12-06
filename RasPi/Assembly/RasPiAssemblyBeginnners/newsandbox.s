/* A simple assembly program */

.global _start

_start:
	mov r0, #45
	mov r7, #1
	swi 0
