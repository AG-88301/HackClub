[org 0x7c00]
KERNEL_OFFSET equ 0x1000
    mov [BOOT_DRIVE], dl
    mov bp, 0x9000
    mov sp, bp

    mov bx, MSG16 
    call print
    call print_nl

    call load_kernel
    call switch32
    jmp $

%include "bootsector/bootsector_print.asm"
%include "bootsector/bootsector_disk.asm"
%include "bootsector/bootsector_gdt.asm"
%include "bootsector/bootsector_print32.asm"
%include "bootsector/bootsector_switch.asm"

[bits 16]
load_kernel:
    mov bx, MSGKERNEL
    call print
    call print_nl

    mov bx, KERNEL_OFFSET
    mov dh, 2
    mov dl, [BOOT_DRIVE]
    call disk_load
    ret

[bits 32]
begin32:
    mov ebx, MSG32
    call print32
    call KERNEL_OFFSET
    jmp $


BOOT_DRIVE db 0
MSG16 db "Started in 16-bit mode", 0
MSG32 db "Loaded 32-bit Protected Mode", 0
MSGKERNEL db "Loaded kernel", 0

times 510 - ($-$$) db 0
dw 0xaa55