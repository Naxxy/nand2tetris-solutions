// ----- C_PUSH constant 111 -----
@111                  // Save value to top of stack
D=A                   // - save literal to D
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_PUSH constant 333 -----
@333                  // Save value to top of stack
D=A                   // - save literal to D
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_PUSH constant 888 -----
@888                  // Save value to top of stack
D=A                   // - save literal to D
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_POP static 8 -----
@16                   // Save segment address to D
D=M
@8                    // - update D to [segment + index]
D=D+A
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Decrement the stack pointer
M=M-1
@SP                   // Save the dereferenced value to D
A=M
D=M
@SP                   // Set A to address (located at @SP + 1)
A=M+1                 // - location above @SP
A=M                   // - value at location above @SP
M=D                   // Save D (popped value) to address (in segment)
// ----- C_POP static 3 -----
@16                   // Save segment address to D
D=M
@3                    // - update D to [segment + index]
D=D+A
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Decrement the stack pointer
M=M-1
@SP                   // Save the dereferenced value to D
A=M
D=M
@SP                   // Set A to address (located at @SP + 1)
A=M+1                 // - location above @SP
A=M                   // - value at location above @SP
M=D                   // Save D (popped value) to address (in segment)
// ----- C_POP static 1 -----
@16                   // Save segment address to D
D=M
@1                    // - update D to [segment + index]
D=D+A
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Decrement the stack pointer
M=M-1
@SP                   // Save the dereferenced value to D
A=M
D=M
@SP                   // Set A to address (located at @SP + 1)
A=M+1                 // - location above @SP
A=M                   // - value at location above @SP
M=D                   // Save D (popped value) to address (in segment)
// ----- C_PUSH static 3 -----
@16                   // Save segment address to D
D=M
@3                    // - update D to [segment + index]
D=D+A
A=D                   // Save segment value to D
D=M
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_PUSH static 1 -----
@16                   // Save segment address to D
D=M
@1                    // - update D to [segment + index]
D=D+A
A=D                   // Save segment value to D
D=M
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- SUB -----
@SP                   // Decrement the stack pointer
M=M-1
@SP                   // Save the dereferenced value to D
A=M
D=M
@SP                   // Decrement the stack pointer
M=M-1
@SP                   // Save the dereferenced value to A
A=M                   // - load pointer address
A=M                   // - load pointer value
D=A-D                 // Perform the subtraction
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_PUSH static 8 -----
@16                   // Save segment address to D
D=M
@8                    // - update D to [segment + index]
D=D+A
A=D                   // Save segment value to D
D=M
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- ADD -----
@SP                   // Decrement the stack pointer
M=M-1
@SP                   // Save the dereferenced value to D
A=M
D=M
@SP                   // Decrement the stack pointer
M=M-1
@SP                   // Save the dereferenced value to A
A=M                   // - load pointer address
A=M                   // - load pointer value
D=A+D                 // Perform the addition
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
(INFINITE_LOOP)       // Infinite Loop
@INFINITE_LOOP
0;JMP
