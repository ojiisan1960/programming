
section .data
section .text

    global _start

_start:
        nop
; put experiments between nops
        mov eax,3
		mov ecx,eax
		shl ecx,1
		add ecx,eax
; put experiments between nops
        nop

section .bss
