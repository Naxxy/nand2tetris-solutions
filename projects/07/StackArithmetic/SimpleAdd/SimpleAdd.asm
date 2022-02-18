// ----- C_PUSH constant 7 -----
@7                    // Save value to top of stack
D=A                   // - save literal to D
@SP                   // - get location of top of stack
A=M
M=D                   // - save D to stack memory location
@SP                   // Increment the stack pointer
M=M+1
// ----- C_PUSH constant 8 -----
@8                    // Save value to top of stack
D=A                   // - save literal to D
@SP                   // - get location of top of stack
A=M
M=D                   // - save D to stack memory location
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
A=M                   // Save the dereferenced value to A
D=M+D                 // Perform the addition
@SP                   // Save the result on the stack (overwrites arg)
A=M
M=D
@SP                   // Increment the stack pointer
M=M+1
(INFINITE_LOOP)       // Infinite Loop
@INFINITE_LOOP
0;JMP
