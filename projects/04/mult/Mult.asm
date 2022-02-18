// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

// CLEAR RESULT BEFORE STARTING
@R2
M=0

// HANDLE ZERO CASE
@R0
D=M
D;JEQ
@R1
D=M
D;JEQ

// MULTIPLY
(LOOP)
    // D = R2
    @R2
    D=M

    // D = R2 + R0
    @R0
    D=D+M

    // R1 -= 1
    @R1
    M=M-1

    // SAVE THE VALUE
    @R2
    M=D

    // JUMP IF R0 == 0
    @R1
    D=M
    @LOOP
    D;JGT

(END)
    @END
    0;JMP
