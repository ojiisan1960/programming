/**** Use pre-indexed addr to move chars ****/
/*											*/

.global _start

_start:
	ldr r1,=letters			@address of letters string
	ldr r3,=numbers			@address of numbers string
	mov r2,#13				@number of letters

_loop:
	ldrb r0,[r1,r2]			@get byte from letters string r1 offset r2
	strb r0,[r3,r2]			@put byte in numbers at r3 offset r2
	subs r2,r2,#1			@decrement r2 
	bpl _loop				@get another byte

_write:
	mov r0,#1				@write to stdout
	mov r2,#26				@length of string
	mov r7,#4				@syscall sys_write
	ldr r1,=numbers			@address of numbers string
	swi 0					@call sys_write

_exit:
	mov r7,#1
	swi 0

.data						@initialized data section
	letters:
		.ascii "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	numbers:
		.ascii "01234567891011121314151617"
