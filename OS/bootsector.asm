[org 0x7c00]
mov bp, 0x9000
mov sp, bp

mov bx, MSG16
call print
call switch32

%include "bootsector_print.asm"
%include "bootsector_gdt.asm"
%include "bootsector_switch.asm"
%include "bootsector_print32.asm"

[bits 32]
begin32:
    mov ebx, MSG32
    call print32

jmp $

MSG16 db "Loaded 16-bit real mode", 0
MSG32 db "Loaded 32-bit protected mode", 0

times 510-($-$$) db 0
dw 0xaa55