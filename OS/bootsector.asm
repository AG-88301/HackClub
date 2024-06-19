[org 0x7c00]

mov bx, HELLO
call print
call print_nl

mov dx, 0x23ff
call print_hex

jmp $

%include "bootsector_print.asm"

; vars
HELLO: db 'Hello World!', 0

times 510-($-$$) db 0
dw 0xaa55
