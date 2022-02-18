// ######### NEW FILE: Sys.vm #########
// ----- Function Sys.init 0 -----
(Sys.init)            // Write function entry
	@SP                   // Set LCL to SP
	D=M
	@LCL
	M=D
// ----- C_PUSH constant 4000 -----
	@4000                 // Save value to top of stack
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
// ----- C_PUSH constant 5000 -----
	@5000                 // Save value to top of stack
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
// ----- CALL Sys.main 0 -----
	@RETURN.0             // Save the return address to the stack
	D=A
	@SP                   // Save the result on the stack (overwrites arg)
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@LCL                  // Get value of LCL pointer
	D=M
	@SP                   // Save the result on the stack (overwrites arg)
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@ARG                  // Get value of ARG pointer
	D=M
	@SP                   // Save the result on the stack (overwrites arg)
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@THIS                 // Get value of THIS pointer
	D=M
	@SP                   // Save the result on the stack (overwrites arg)
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@THAT                 // Get value of THAT pointer
	D=M
	@SP                   // Save the result on the stack (overwrites arg)
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@SP                   // Reposition ARG to (SP - 5 - nArgs)
	A=M-1
	A=A-1
	A=A-1
	A=A-1
	A=A-1
	D=A                   // - Save address to D then set ARG to D
	@ARG
	M=D
	@SP                   // Set LCL to value of SP
	D=M
	@LCL
	M=D
	M=D                   // Jump to callee
(RETURN.0)            // Set the label for the function call return address
// ----- C_POP temp 1 -----
	@5                    // Save segment address to D
	D=A
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
// ----- LABEL -----
(LOOP)                // Write label
// ----- GOTO -----
	@LOOP                 // - load jump address
	0;JMP                 // - unconditional jump
// ----- Function Sys.main 5 -----
(Sys.main)            // Write function entry
	@SP                   // Set LCL to SP
	D=M
	@LCL
	M=D
	@SP                   // Push 0 to LCL (loop 0 of 5)
	A=M
	M=0
	@SP                   // Increment the stack pointer
	M=M+1
	@SP                   // Push 0 to LCL (loop 0 of 5)
	A=M
	M=0
	@SP                   // Increment the stack pointer
	M=M+1
	@SP                   // Push 0 to LCL (loop 0 of 5)
	A=M
	M=0
	@SP                   // Increment the stack pointer
	M=M+1
	@SP                   // Push 0 to LCL (loop 0 of 5)
	A=M
	M=0
	@SP                   // Increment the stack pointer
	M=M+1
	@SP                   // Push 0 to LCL (loop 0 of 5)
	A=M
	M=0
	@SP                   // Increment the stack pointer
	M=M+1
// ----- C_PUSH constant 4001 -----
	@4001                 // Save value to top of stack
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
// ----- C_PUSH constant 5001 -----
	@5001                 // Save value to top of stack
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
// ----- C_PUSH constant 200 -----
	@200                  // Save value to top of stack
	D=A                   // - save literal to D
	@SP                   // Save the result on the stack (overwrites arg)
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
// ----- C_POP local 1 -----
	@LCL                  // Save segment address to D
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
// ----- C_PUSH constant 40 -----
	@40                   // Save value to top of stack
	D=A                   // - save literal to D
	@SP                   // Save the result on the stack (overwrites arg)
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
// ----- C_POP local 2 -----
	@LCL                  // Save segment address to D
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
// ----- C_PUSH constant 6 -----
	@6                    // Save value to top of stack
	D=A                   // - save literal to D
	@SP                   // Save the result on the stack (overwrites arg)
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
// ----- C_POP local 3 -----
	@LCL                  // Save segment address to D
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
// ----- C_PUSH constant 123 -----
	@123                  // Save value to top of stack
	D=A                   // - save literal to D
	@SP                   // Save the result on the stack (overwrites arg)
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
// ----- CALL Sys.add12 1 -----
	@RETURN.1             // Save the return address to the stack
	D=A
	@SP                   // Save the result on the stack (overwrites arg)
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@LCL                  // Get value of LCL pointer
	D=M
	@SP                   // Save the result on the stack (overwrites arg)
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@ARG                  // Get value of ARG pointer
	D=M
	@SP                   // Save the result on the stack (overwrites arg)
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@THIS                 // Get value of THIS pointer
	D=M
	@SP                   // Save the result on the stack (overwrites arg)
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@THAT                 // Get value of THAT pointer
	D=M
	@SP                   // Save the result on the stack (overwrites arg)
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@SP                   // Reposition ARG to (SP - 5 - nArgs)
	A=M-1
	A=A-1
	A=A-1
	A=A-1
	A=A-1
	A=A-1
	D=A                   // - Save address to D then set ARG to D
	@ARG
	M=D
	@SP                   // Set LCL to value of SP
	D=M
	@LCL
	M=D
	M=D                   // Jump to callee
(RETURN.1)            // Set the label for the function call return address
// ----- C_POP temp 0 -----
	@5                    // Save segment address to D
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
// ----- C_PUSH local 1 -----
	@LCL                  // Save segment address to D
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
// ----- C_PUSH local 2 -----
	@LCL                  // Save segment address to D
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
// ----- C_PUSH local 3 -----
	@LCL                  // Save segment address to D
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
// ----- C_PUSH local 4 -----
	@LCL                  // Save segment address to D
	D=M
	@4                    // - update D to [segment + index]
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
// ----- RETURN -----
	@LCL                  // Save LCL to TEMP
	D=M
	@TEMP
	M=D
	@LCL                  // Get return address
	A=M-1                 // - return address = LCL - 5
	A=A-1
	A=A-1
	A=A-1
	A=A-1
	D=A
	@TEMP                 // Save return address to TEMP + 1
	A=A+1
	M=D
	@SP                   // Decrement the stack pointer
	M=M-1
	@SP                   // Save the dereferenced value to D
	A=M
	D=M
	@ARG                  // Save return value to ARG address
	A=M
	M=D
	@ARG                  // Reset @SP to @ARG + 1
	D=M
	@SP
	M=D+1
	@TEMP                 // Get THAT from frame
	M=M-1
	A=M
	D=M                   // Restore THAT value from frame
	@THAT
	M=D
	@TEMP                 // Get THIS from frame
	M=M-1
	A=M
	D=M                   // Restore THIS value from frame
	@THIS
	M=D
	@TEMP                 // Get ARG from frame
	M=M-1
	A=M
	D=M                   // Restore ARG value from frame
	@ARG
	M=D
	@TEMP                 // Get LCL from frame
	M=M-1
	A=M
	D=M                   // Restore LCL value from frame
	@LCL
	M=D
// ----- Function Sys.add12 0 -----
(Sys.add12)           // Write function entry
	@SP                   // Set LCL to SP
	D=M
	@LCL
	M=D
// ----- C_PUSH constant 4002 -----
	@4002                 // Save value to top of stack
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
// ----- C_PUSH constant 5002 -----
	@5002                 // Save value to top of stack
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
// ----- C_PUSH constant 12 -----
	@12                   // Save value to top of stack
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
// ----- RETURN -----
	@LCL                  // Save LCL to TEMP
	D=M
	@TEMP
	M=D
	@LCL                  // Get return address
	A=M-1                 // - return address = LCL - 5
	A=A-1
	A=A-1
	A=A-1
	A=A-1
	D=A
	@TEMP                 // Save return address to TEMP + 1
	A=A+1
	M=D
	@SP                   // Decrement the stack pointer
	M=M-1
	@SP                   // Save the dereferenced value to D
	A=M
	D=M
	@ARG                  // Save return value to ARG address
	A=M
	M=D
	@ARG                  // Reset @SP to @ARG + 1
	D=M
	@SP
	M=D+1
	@TEMP                 // Get THAT from frame
	M=M-1
	A=M
	D=M                   // Restore THAT value from frame
	@THAT
	M=D
	@TEMP                 // Get THIS from frame
	M=M-1
	A=M
	D=M                   // Restore THIS value from frame
	@THIS
	M=D
	@TEMP                 // Get ARG from frame
	M=M-1
	A=M
	D=M                   // Restore ARG value from frame
	@ARG
	M=D
	@TEMP                 // Get LCL from frame
	M=M-1
	A=M
	D=M                   // Restore LCL value from frame
	@LCL
	M=D
(INFINITE_LOOP)       // Infinite Loop
	@INFINITE_LOOP
	0;JMP
