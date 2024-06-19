mov ah, 0x0e ; tty

mov al, [text]
int 0x10 

mov bx, 0x7c0 
mov ds, bx
mov al, [text]
int 0x10

mov al, [es:text]
int 0x10

mov bx, 0x7c0
mov es, bx
mov al, [es:text]
int 0x10

jmp $

text:
    db "X"

times 510 - ($-$$) db 0
dw 0xaa55
