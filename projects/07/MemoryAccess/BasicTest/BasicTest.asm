// ----- C_PUSH constant 10 -----
@10                   // Save value to top of stack
D=A                   // - save literal to D
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_POP local 0 -----
@LCL                  // Save segment address to D
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
// ----- C_PUSH constant 21 -----
@21                   // Save value to top of stack
D=A                   // - save literal to D
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_PUSH constant 22 -----
@22                   // Save value to top of stack
D=A                   // - save literal to D
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_POP argument 2 -----
@ARG                  // Save segment address to D
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
// ----- C_POP argument 1 -----
@ARG                  // Save segment address to D
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
// ----- C_PUSH constant 36 -----
@36                   // Save value to top of stack
D=A                   // - save literal to D
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_POP this 6 -----
@THIS                 // Save segment address to D
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
// ----- C_PUSH constant 42 -----
@42                   // Save value to top of stack
D=A                   // - save literal to D
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_PUSH constant 45 -----
@45                   // Save value to top of stack
D=A                   // - save literal to D
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_POP that 5 -----
@THAT                 // Save segment address to D
D=M
@5                    // - update D to [segment + index]
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
// ----- C_PUSH constant 510 -----
@510                  // Save value to top of stack
D=A                   // - save literal to D
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_POP temp 6 -----
@5                    // Save segment address to D
D=A
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
// ----- C_PUSH local 0 -----
@LCL                  // Save segment address to D
D=M
A=D                   // Save segment value to D
D=M
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
// ----- C_PUSH that 5 -----
@THAT                 // Save segment address to D
D=M
@5                    // - update D to [segment + index]
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
// ----- C_PUSH this 6 -----
@THIS                 // Save segment address to D
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
// ----- C_PUSH this 6 -----
@THIS                 // Save segment address to D
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
// ----- C_PUSH temp 6 -----
@5                    // Save segment address to D
D=A
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
