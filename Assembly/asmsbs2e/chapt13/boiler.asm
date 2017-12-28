; Source name      : BOILER.ASM
; Executable name  : BOILER -- though this isn't intended to be run!
; Version          : 1.0
; Created date     : 10/1/1999
; Last update      : 10/18/1999
; Author           : Jeff Duntemann
; Description      : A "skeleton" program in assembly for Linux, using NASM 0.98
;
; Build using these commands:
;  nasm -f elf boiler.asm
;  gcc boiler.o -o boiler
;
; HOWEVER, the program as given here is "boilerplate" and has nothing "useful"
;  to do. The idea is to give you a head start on new projects, by providing
;  the things that every (or nearly every) simple Linux assembly program must
;  have.
[SECTION .text]       ; Section containing code
global main           ; Required so linker can find entry point
main:
      push ebp        ; Set up stack frame
      mov ebp,esp     ; ebp is our "thumb" in the stack
      push ebx        ; Program must preserve ebp, ebx, esi, & edi
      push esi
      push edi
      ;;; Everything before this is boilerplate; use it for all ordinary apps!
      ;;; This is where you put your own code!
      ;;; Everything after this is boilerplate; use it for all ordinary apps!
      pop edi         ; Restore saved registers
      pop esi
      pop ebx
      mov esp,ebp     ; Destroy stack frame before returning
      pop ebp
      ret             ; Return control to Linux
[SECTION .data]      ; Section containing initialized data
[SECTION .bss]       ; Section containing uninitialized data
