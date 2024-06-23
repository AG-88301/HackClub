#include "../drivers/screen.c"

void main() {
    clear_screen();
    kprint("Hello World!");
    kprint("Goodbye World!");
    kprint("looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong");

    kprint("\n");
    kprint("Line\nBreak");
    kprint("ok");
}