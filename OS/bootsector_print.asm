print: pusha

start:
    mov al, [bx]
    cmp al, 0 
    je done

    mov ah, 0x0e
    int 0x10 
    
    add bx, 1
    jmp start

print_nl:
    pusha
    
    mov ah, 0x0e
    mov al, 0x0a 
    int 0x10
    mov al, 0x0d
    int 0x10
    
    jmp done

print_hex:
    pusha
    mov cx, 0 
    jmp cast_hex

cast_hex:
    cmp cx, 4 
    je end_hex
    
    mov ax, dx 
    and ax, 0x000f 
    add al, 0x30
    cmp al, 0x39 
    jle store_hex
    add al, 7 

store_hex:
    mov bx, HEX_OUT + 5 
    sub bx, cx 
    mov [bx], al 
    ror dx, 4 

    add cx, 1
    jmp cast_hex

end_hex:
    mov bx, HEX_OUT
    call print

    jmp done;

done:
    popa
    ret

HEX_OUT: db '0x0000',0