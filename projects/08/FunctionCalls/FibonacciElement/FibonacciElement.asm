// @@@@@@@@ STANDARD MAPPING @@@@@@@@
	@256                  // Write @SP standard mapping value
	D=A
	@SP
	M=D
// ----- CALL Sys.init 0 -----
	@RETURN.0             // Save the return address to D
	D=A
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@LCL                  // Get value of LCL pointer
	D=M
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@ARG                  // Get value of ARG pointer
	D=M
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@THIS                 // Get value of THIS pointer
	D=M
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@THAT                 // Get value of THAT pointer
	D=M
	@SP                   // Save D to the stack
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
	@Sys.init             // Jump to callee
	0;JMP
(RETURN.0)            // Set the label for the function call return address
// ######### NEW FILE: Main.vm #########
// ----- Function Main.fibonacci 0 -----
(Main.fibonacci)      // Write function entry
	@SP                   // Set LCL to SP
	D=M
	@LCL
	M=D
// ----- C_PUSH argument 0 -----
	@ARG                  // Save segment address to D
	D=M
	A=D                   // Save segment value to D
	D=M
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
// ----- C_PUSH constant 2 -----
	@2                    // Save value to top of stack
	D=A                   // - save literal to D
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
// ----- LT -----
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
	D=A-D                 // Check less than
	@ARITHTRUE0           // - true jump location
	D;JLT                 // - jump if true
	D=0                   // - save false value
	@CONTINUE0            // - false jump location
	0;JMP                 // - jump over true case
	(ARITHTRUE0)          // - handle true case
	D=-1                  // - save true value
	(CONTINUE0)
	@SP                   // Save D to the stack
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
	@IF_TRUE              // - save jump location
	D;JNE                 // - jump if non-zero
// ----- GOTO -----
	@IF_FALSE             // - load jump address
	0;JMP                 // - unconditional jump
// ----- LABEL -----
(IF_TRUE)             // Write label
// ----- C_PUSH argument 0 -----
	@ARG                  // Save segment address to D
	D=M
	A=D                   // Save segment value to D
	D=M
	@SP                   // Save D to the stack
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
	@TEMP                 // Jump to return address (from TEMP + 1)
	A=A+1
	A=M
	0;JMP
// ----- LABEL -----
(IF_FALSE)            // Write label
// ----- C_PUSH argument 0 -----
	@ARG                  // Save segment address to D
	D=M
	A=D                   // Save segment value to D
	D=M
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
// ----- C_PUSH constant 2 -----
	@2                    // Save value to top of stack
	D=A                   // - save literal to D
	@SP                   // Save D to the stack
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
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
// ----- CALL Main.fibonacci 1 -----
	@RETURN.1             // Save the return address to D
	D=A
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@LCL                  // Get value of LCL pointer
	D=M
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@ARG                  // Get value of ARG pointer
	D=M
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@THIS                 // Get value of THIS pointer
	D=M
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@THAT                 // Get value of THAT pointer
	D=M
	@SP                   // Save D to the stack
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
	@Main.fibonacci       // Jump to callee
	0;JMP
(RETURN.1)            // Set the label for the function call return address
// ----- C_PUSH argument 0 -----
	@ARG                  // Save segment address to D
	D=M
	A=D                   // Save segment value to D
	D=M
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
// ----- C_PUSH constant 1 -----
	@1                    // Save value to top of stack
	D=A                   // - save literal to D
	@SP                   // Save D to the stack
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
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
// ----- CALL Main.fibonacci 1 -----
	@RETURN.2             // Save the return address to D
	D=A
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@LCL                  // Get value of LCL pointer
	D=M
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@ARG                  // Get value of ARG pointer
	D=M
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@THIS                 // Get value of THIS pointer
	D=M
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@THAT                 // Get value of THAT pointer
	D=M
	@SP                   // Save D to the stack
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
	@Main.fibonacci       // Jump to callee
	0;JMP
(RETURN.2)            // Set the label for the function call return address
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
	@SP                   // Save D to the stack
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
	@TEMP                 // Jump to return address (from TEMP + 1)
	A=A+1
	A=M
	0;JMP
// ######### NEW FILE: Sys.vm #########
// ----- Function Sys.init 0 -----
(Sys.init)            // Write function entry
	@SP                   // Set LCL to SP
	D=M
	@LCL
	M=D
// ----- C_PUSH constant 4 -----
	@4                    // Save value to top of stack
	D=A                   // - save literal to D
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
// ----- CALL Main.fibonacci 1 -----
	@RETURN.3             // Save the return address to D
	D=A
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@LCL                  // Get value of LCL pointer
	D=M
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@ARG                  // Get value of ARG pointer
	D=M
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@THIS                 // Get value of THIS pointer
	D=M
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
	@THAT                 // Get value of THAT pointer
	D=M
	@SP                   // Save D to the stack
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
	@Main.fibonacci       // Jump to callee
	0;JMP
(RETURN.3)            // Set the label for the function call return address
// ----- LABEL -----
(WHILE)               // Write label
// ----- GOTO -----
	@WHILE                // - load jump address
	0;JMP                 // - unconditional jump
