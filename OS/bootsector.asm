[org 0x7c00]
mov bp, 0x8000
mov sp, bp

mov bx, 0x9000
mov dh, 2
call disk_load

; test
mov bx, MESSAGE
call print

call print_nl

mov dx, [0x9000]
call print_hex

call print_nl

mov dx, [0x9000 + 512]
call print_hex

jmp $

%include "bootsector_print.asm"
%include "bootsector_disk.asm"

MESSAGE: db 'Retrieved from disk:', 0

times 510 - ($-$$) db 0
dw 0xaa55

; test data
times 256 dw 0xde43
times 256 dw 0xff1f
