[org 0x7c00]
KERNEL_OFFSET equ 0x1000

mov [BOOT_DRIVE], dl
mov bp, 0x9000
mov sp, bp

mov bx, MSG_REAL_MODE 
call print
call print_nl

call load_kernel
call switch32
jmp $

%include "bootsector_print.asm"
%include "bootsector_disk.asm"
%include "bootsector_gdt.asm"
%include "bootsector_print32.asm"
%include "bootsector_switch.asm"

[bits 16]
load_kernel:
    mov bx, MSG_LOAD_KERNEL
    call print
    call print_nl

    mov bx, KERNEL_OFFSET
    mov dh, 2
    mov dl, [BOOT_DRIVE]
    call disk_load
    ret

[bits 32]
begin32:
    mov ebx, MSG_PROT_MODE
    call print32
    call KERNEL_OFFSET
    jmp $


BOOT_DRIVE db 0
MSG_REAL_MODE db "Started in 16-bit mode", 0
MSG_PROT_MODE db "Loaded 32-bit Protected Mode", 0
MSG_LOAD_KERNEL db "Loaded kernel", 0

times 510 - ($-$$) db 0
dw 0xaa55