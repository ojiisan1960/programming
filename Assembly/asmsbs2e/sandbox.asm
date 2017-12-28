
section .data
section .text

    global _start

_start:
        nop
; put experiments between nops
mov eax, 0FFFFFFFFh
mov ebx, 02Dh
dec ebx
inc eax

; put experiments between nops
        nop

section .bss
