	.file	"dateis.c"
	.section	.rodata
.LC0:
	.string	"The date is: %s"
	.text
.globl main
	.type	main, @function
main:
	leal	4(%esp), %ecx
	andl	$-16, %esp
	pushl	-4(%ecx)
	pushl	%ebp
	movl	%esp, %ebp
	pushl	%ecx
	subl	$36, %esp
	leal	-8(%ebp), %eax
	movl	%eax, (%esp)
	call	time
	leal	-8(%ebp), %eax
	movl	%eax, (%esp)
	call	ctime
	movl	%eax, 4(%esp)
	movl	$.LC0, (%esp)
	call	printf
	movl	$0, (%esp)
	call	exit
	.size	main, .-main
	.ident	"GCC: (Ubuntu 4.3.3-5ubuntu4) 4.3.3"
	.section	.note.GNU-stack,"",@progbits
