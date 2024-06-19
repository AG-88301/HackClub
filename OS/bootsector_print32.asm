[bits 32]

VIDEO equ 0xb8000
COLOR equ 0x5f

print32:
    pusha
    mov edx, VIDEO

print32loop:
    mov al, [ebx]
    mov ah, COLOR

    cmp al, 0
    je done

    mov [edx], ax
    add ebx, 1
    add edx, 2

    jmp print32loop
