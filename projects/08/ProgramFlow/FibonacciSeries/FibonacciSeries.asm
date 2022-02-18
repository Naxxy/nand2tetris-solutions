// ----- C_PUSH argument 1 -----
@ARG                  // Save segment address to D
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
// ----- C_PUSH constant 0 -----
@0                    // Save value to top of stack
D=A                   // - save literal to D
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_POP that 0 -----
@THAT                 // Save segment address to D
D=M
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
// ----- C_PUSH constant 1 -----
@1                    // Save value to top of stack
D=A                   // - save literal to D
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_POP that 1 -----
@THAT                 // Save segment address to D
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
// ----- C_PUSH argument 0 -----
@ARG                  // Save segment address to D
D=M
A=D                   // Save segment value to D
D=M
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_PUSH constant 2 -----
@2                    // Save value to top of stack
D=A                   // - save literal to D
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
// ----- C_POP argument 0 -----
@ARG                  // Save segment address to D
D=M
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
// ----- LABEL -----
(MAIN_LOOP_START)     // Write label
// ----- C_PUSH argument 0 -----
@ARG                  // Save segment address to D
D=M
A=D                   // Save segment value to D
D=M
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- IF-GOTO -----
@SP                   // Decrement the stack pointer
M=M-1
@SP                   // Save the dereferenced value to D
A=M
D=M
@COMPUTE_ELEMENT      // - save jump location
D;JNE                 // - jump if non-zero
// ----- GOTO -----
@END_PROGRAM          // - load jump address
0;JMP                 // - unconditional jump
// ----- LABEL -----
(COMPUTE_ELEMENT)     // Write label
// ----- C_PUSH that 0 -----
@THAT                 // Save segment address to D
D=M
A=D                   // Save segment value to D
D=M
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_PUSH that 1 -----
@THAT                 // Save segment address to D
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
// ----- C_POP that 2 -----
@THAT                 // Save segment address to D
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
// ----- C_PUSH constant 1 -----
@1                    // Save value to top of stack
D=A                   // - save literal to D
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
// ----- C_PUSH argument 0 -----
@ARG                  // Save segment address to D
D=M
A=D                   // Save segment value to D
D=M
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_PUSH constant 1 -----
@1                    // Save value to top of stack
D=A                   // - save literal to D
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
// ----- C_POP argument 0 -----
@ARG                  // Save segment address to D
D=M
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
// ----- GOTO -----
@MAIN_LOOP_START      // - load jump address
0;JMP                 // - unconditional jump
// ----- LABEL -----
(END_PROGRAM)         // Write label
(INFINITE_LOOP)       // Infinite Loop
@INFINITE_LOOP
0;JMP
