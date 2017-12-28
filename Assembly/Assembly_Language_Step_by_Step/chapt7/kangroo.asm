
section .data
  Snippet db "KANGAROO"
section .text

    global _start

_start:
        nop
; put experiments between nops
    mov ebx,Snippet         ;put the address of Snippet here
    mov eax,8               ;number of characters in Snippet
  DoMore: add byte [ebx],32 ; add 32 to change character case?
    inc ebx                 ; increment ebx
    dec eax                 ; decrement counter eax
    jnz DoMore              ; loop back to DoMore while eax is not 0



; put experiments between nops
        nop

section .bss
