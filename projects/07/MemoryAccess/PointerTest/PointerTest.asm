// ----- C_PUSH constant 3030 -----
@3030                 // Save value to top of stack
D=A                   // - save literal to D
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_POP pointer 0 -----
@THIS                 // Save pointer address 0 to D
D=A
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
// ----- C_PUSH constant 3040 -----
@3040                 // Save value to top of stack
D=A                   // - save literal to D
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_POP pointer 1 -----
@THAT                 // Save pointer address 1 to D
D=A
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
// ----- C_PUSH constant 32 -----
@32                   // Save value to top of stack
D=A                   // - save literal to D
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_POP this 2 -----
@THIS                 // Save segment address to D
D=M
@2                    // - update D to [segment + index]
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
// ----- C_PUSH constant 46 -----
@46                   // Save value to top of stack
D=A                   // - save literal to D
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_POP that 6 -----
@THAT                 // Save segment address to D
D=M
@6                    // - update D to [segment + index]
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
// ----- C_PUSH pointer 0 -----
@THIS                 // Save pointer address 0 to D
D=A
A=D                   // Save segment value to D
D=M
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_PUSH pointer 1 -----
@THAT                 // Save pointer address 1 to D
D=A
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
// ----- C_PUSH this 2 -----
@THIS                 // Save segment address to D
D=M
@2                    // - update D to [segment + index]
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
// ----- C_PUSH that 6 -----
@THAT                 // Save segment address to D
D=M
@6                    // - update D to [segment + index]
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
