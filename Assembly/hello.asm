section .data
  hello:    db 'Hello World!', 10   ; string
  helloLen: equ $-hello             ; length of the string

section .text
  global _start

_start:
  mov eax,4                         ; system call for write
  mov ebx,1                         ; file descriptor, stdout
  mov ecx,hello                     ; put the offset of hello in ecx
  mov edx,helloLen                  ; helloLen is a constant, don't need
                                    ; use mov edx,[helloLen] to get the
                                    ; contents
  int 80h                           ; call the kernel

  mov eax,1                         ;system call for exit
  mov ebx,0                         ;exit with return code 0
  int 80h
