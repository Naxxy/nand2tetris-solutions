// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.


(LOOP)

    // i = 8192 // result of 256 * 512
    @8192
    D=A
    @i
    M=D

    // pointer = SCREEN (0, 0)
    @SCREEN
    D=A
    @pointer
    M=D

    // set colour to black
    @color
    M=-1

    // check input
    @KBD
    D=M
    @DRAW
    D;JNE

    // set colour to white
    @color
    M=0

(DRAW)

    // RAM[pointer] = color
    @color
    D=M
    @pointer
    A=M
    M=D

    // pointer += 1
    @pointer
    M=M+1

    // i -= 1
    @i
    M=M-1

    // Repeat draw if i > 0
    D=M
    @DRAW
    D;JGT

    // End draw if i == 0
    @LOOP
    0;JEQ
