#define VIDEO_ADDRESS 0xb8000
#define MAX_ROWS 25
#define MAX_COLS 80
#define WHITE_ON_BLACK 0x0f

#define CTRL 0x3d4
#define DATA 0x3d5

#include "port.c"

int get_cursor_offset() {
    port_byte_out(CTRL, 14);
    int offset = port_byte_in(DATA) << 8;
    port_byte_out(CTRL, 15);
    offset += port_byte_in(DATA);
    return offset * 2;
}

void set_cursor_offset(int offset) {
    offset /= 2;
    port_byte_out(CTRL, 14);
    port_byte_out(DATA, (unsigned char)(offset >> 8));
    port_byte_out(CTRL, 15);
    port_byte_out(DATA, (unsigned char)(offset & 0xff));
}

void clear_screen() {
    int screen_size = MAX_COLS * MAX_ROWS;
    int i;
    char *screen = VIDEO_ADDRESS;

    for (i = 0; i < screen_size; i++) {
        screen[i*2] = ' ';
        screen[i*2+1] = WHITE_ON_BLACK;
    }
    set_cursor_offset(get_offset(0, 0));
}

void kprint(char *string) {    
    int i = 0;
    char *screen = VIDEO_ADDRESS;
    while (string[i] != 0) {
        int cursorPos = get_cursor_offset();
        if (string[i] == 10) {
            int currOffset = get_cursor_offset();
            set_cursor_offset(get_offset(get_row(currOffset) + 1, 0));
        } else {
            screen[cursorPos] = string[i];
            screen[cursorPos + 1] = WHITE_ON_BLACK;
            set_cursor_offset(cursorPos + 2);
        }
        i += 1;
    }
    int currOffset = get_cursor_offset();
    set_cursor_offset(get_offset(get_row(currOffset) + 1, 0));
    return;
}

int get_offset(int row, int col) { return 2 * (row * MAX_COLS + col); }
get_row(int offset) { return offset / (2 * MAX_COLS); }
get_col(int offset) { return offset % (2 * MAX_COLS); }