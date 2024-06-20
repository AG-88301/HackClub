all: run

op/kernel.bin: op/kernel_entry.o op/kernel.o
	/usr/local/i386elfgcc/bin/i386-elf-ld -o $@ -Ttext 0x1000 $^ --oformat binary

op/kernel_entry.o: bootsector/kernel_entry.asm
	nasm $< -f elf -o $@

op/kernel.o: kernel/kernel.c
	/usr/local/i386elfgcc/bin/i386-elf-gcc -ffreestanding -c $< -o $@

op/kernel.dis: op/kernel.bin
	ndisasm -b 32 $< > $@

bootsect.bin: bootsector/bootsector.asm
	nasm $< -f bin -o $@

op/os_image.bin: bootsector.bin op/kernel.bin
	cat $^ > $@

run: op/os_image.bin
	qemu-system-i386 -fda $<

clean:
	rm *.bin *.o *.dis