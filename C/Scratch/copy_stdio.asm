	.file	"copy_stdio.c"
	.section	.rodata
.LC0:
	.string	"r"
.LC1:
	.string	"file.in"
.LC2:
	.string	"w"
.LC3:
	.string	"file.out"
	.text
	.globl	main
	.type	main, @function
main:
.LFB2:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$32, %rsp
	movl	$.LC0, %esi
	movl	$.LC1, %edi
	call	fopen
	movq	%rax, -16(%rbp)
	movl	$.LC2, %esi
	movl	$.LC3, %edi
	call	fopen
	movq	%rax, -8(%rbp)
	jmp	.L2
.L3:
	movq	-8(%rbp), %rdx
	movl	-20(%rbp), %eax
	movq	%rdx, %rsi
	movl	%eax, %edi
	call	fputc
.L2:
	movq	-16(%rbp), %rax
	movq	%rax, %rdi
	call	fgetc
	cmpl	$-1, %eax
	setne	%al
	movzbl	%al, %eax
	movl	%eax, -20(%rbp)
	cmpl	$0, -20(%rbp)
	jne	.L3
	movl	$0, %edi
	call	exit
	.cfi_endproc
.LFE2:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.5) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
