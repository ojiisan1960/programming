
section .bss
    Buff resb 1

section .data

section .text
    global _start

_start:
        nop                 ;keeps gdb happy

Read:   mov eax, 3          ; syscall sys_read
        mov ebx, 0          ; file descriptor stdin
        mov ecx,Buff        ; address of buffer to read from
        mov edx, 1          ; read 1 char at a time
        int 80h             ; call sys_read

        cmp eax, 0          ; compare sys_read return value
        je  Exit            ; if 0 then its EOF - end of file
        cmp byte [Buff],61h ; test char in the buffer against 'a'
        jb Write            ; if below 'a' in ASCII chart
                            ;   not a lower case character, write it out
        cmp byte [Buff],7Ah ; test char in buffer against 'z'
        ja  Write           ; if above 'z' in ASCII chart
                            ;   not a lower case character, write it out
        sub byte [Buff],20h ; subtract 20h to make char upper case
                            ;   then write it out
Write:  mov eax, 4          ; syscall sys_write
        mov ebx, 1          ; file descriptor stdout
        mov ecx,Buff        ; address of buffer
        mov edx,1           ; write 1 char 
        int 80h             ; call sys_write
        jmp Read            ; go back to read another char

Exit:    mov eax,1           ; syscall sys_exit
        mov ebx,0           ; return code
        int 80h             ; syscall sys_exit to exit the program

    
        
        
