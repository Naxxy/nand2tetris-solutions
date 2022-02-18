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
// ######### NEW FILE: SimpleFunction.vm #########
// ----- Function SimpleFunction.test 3 -----
(SimpleFunction.test) // Write function entry
	@SP                   // Set LCL to SP
	D=M
	@LCL
	M=D
	@SP                   // Push 0 to LCL (loop 0 of 3)
	A=M
	M=0
	@SP                   // Increment the stack pointer
	M=M+1
	@SP                   // Push 0 to LCL (loop 0 of 3)
	A=M
	M=0
	@SP                   // Increment the stack pointer
	M=M+1
	@SP                   // Push 0 to LCL (loop 0 of 3)
	A=M
	M=0
	@SP                   // Increment the stack pointer
	M=M+1
// ----- C_PUSH local 0 -----
	@LCL                  // Save segment address to D
	D=M
	A=D                   // Save segment value to D
	D=M
	@SP                   // Save D to the stack
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
	@SP                   // Save D to the stack
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
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
// ----- NOT -----
	@SP                   // Decrement the stack pointer
	M=M-1
	@SP                   // Save the dereferenced value to D
	A=M
	D=!M                  // Perform the bit-wise NOT
	@SP                   // Save D to the stack
	A=M
	M=D
	@SP                   // Increment the stack pointer
	M=M+1
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
// ----- C_PUSH argument 1 -----
	@ARG                  // Save segment address to D
	D=M
	@1                    // - update D to [segment + index]
	D=D+A
	A=D                   // Save segment value to D
	D=M
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
