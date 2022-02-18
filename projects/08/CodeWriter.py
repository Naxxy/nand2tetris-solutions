#!/usr/bin/env python
from Parser import CommandType



# TODO
class CodeWriter:
    fp = None
    arithmetic_jump_counter = 0
    return_counter = 0
    with_bootstrapping = False

    def __init__(self, filename: str):
        self.fp = open(filename, 'w')
        self.arithmetic_jump_counter = 0
        self.return_counter = 0
        self.with_bootstrapping = False

        #  Write standard mapping / bootstrapping code
        if not self.with_bootstrapping:
            self.fp.write("// @@@@@@@@ STANDARD MAPPING @@@@@@@@\n".format(filename))
            self.fp.write(self._formatted_string('@256', 'Write @SP standard mapping value'))
            self.fp.write(self._formatted_string('D=A'))
            self.fp.write(self._formatted_string('@SP'))
            self.fp.write(self._formatted_string('M=D'))

            self.writeCall('Sys.init', 0)


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type != None or exc_value != None or traceback != None:
            print('Exiting context: ', self, exc_type, exc_value, traceback)

        self.fp.close()
        return True # suppress errors

    #
    # CLASS METHODS
    #

    # TODO
    def setFileName(self, filename: str):
        self.fp.write("// ######### NEW FILE: {} #########\n".format(filename))

    def close(self):
        if self.with_bootstrapping:
            self.fp.write(self._formatted_string('(INFINITE_LOOP)', 'Infinite Loop', indented=False))
            self.fp.write(self._formatted_string('@INFINITE_LOOP'))
            self.fp.write(self._formatted_string('0;JMP'))

        self.fp.close()

    #
    # ARITHMETIC & STACK
    #

    def writeArithmetic(self, command: str):
        # NOTE: True mapped to -1, False mapped to 0
        def _add():
            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_D()

            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_A(False)

            self.fp.write(self._formatted_string('D=A+D', 'Perform the addition'))

            self._save_D_to_stack()
            self._increment_stack_pointer()

        def _sub():
            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_D()

            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_A(False)

            self.fp.write(self._formatted_string('D=A-D', 'Perform the subtraction'))

            self._save_D_to_stack()
            self._increment_stack_pointer()

        def _neg():
            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_D()

            self.fp.write(self._formatted_string('D=-D', 'Perform the negation'))

            self._save_D_to_stack()
            self._increment_stack_pointer()

        def _eq():
            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_D()

            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_A(False)

            self._save_comparison_to_D('JEQ', 'Check equality')

            self._save_D_to_stack()
            self._increment_stack_pointer()

        def _gt():
            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_D()

            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_A(False)

            self._save_comparison_to_D('JGT', 'Check greater than')

            self._save_D_to_stack()
            self._increment_stack_pointer()

        def _lt():
            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_D()

            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_A(False)

            self._save_comparison_to_D('JLT', 'Check less than')

            self._save_D_to_stack()
            self._increment_stack_pointer()

        def _and():
            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_D()

            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_A(False)

            self.fp.write(self._formatted_string('D=A&D', 'Perform the bit-wise AND'))

            self._save_D_to_stack()
            self._increment_stack_pointer()

        def _or():
            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_D()

            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_A(False)

            self.fp.write(self._formatted_string('D=A|D', 'Perform the bit-wise OR'))

            self._save_D_to_stack()
            self._increment_stack_pointer()

        def _not():
            self._decrement_stack_pointer()
            self.fp.write(self._formatted_string('@SP', 'Save the dereferenced value to D'))
            self.fp.write(self._formatted_string('A=M'))
            self.fp.write(self._formatted_string('D=!M', 'Perform the bit-wise NOT'))

            self._save_D_to_stack()
            self._increment_stack_pointer()

        # Write section comment & execute
        self.fp.write("// ----- {} -----\n".format(command.upper()))
        if command == 'add':        _add()
        elif command == 'sub':      _sub()
        elif command == 'neg':      _neg()
        elif command == 'eq':       _eq()
        elif command == 'gt':       _gt()
        elif command == 'lt':       _lt()
        elif command == 'and':      _and()
        elif command == 'or':       _or()
        elif command == 'not':      _not()
        else:
            self.fp.write("// ----- {} UNIMPLEMENTED -----\n".format(command.upper()))

    def writePushPop(self, commandType: CommandType, segment: str, index: int):
        def _push_constant():
            # Load value
            self.fp.write(self._formatted_string('@{}'.format(index), 'Save value to top of stack'))
            self.fp.write(self._formatted_string('D=A', '- save literal to D'))

            # Save value
            self._save_D_to_stack()
            self._increment_stack_pointer()

        def _push_named_segment():
            # Get segment address
            if segment == 'pointer':
                address = 'THIS' if index == 0 else 'THAT'
                self.fp.write(self._formatted_string('@{}'.format(address), 'Save pointer address {} to D'.format(index)))
                self.fp.write(self._formatted_string('D=A'))
            else:
                address = segment_to_address[segment]
                self._set_D_to_segment_address(address, index, is_temp=(segment == 'temp'))

            # Save segment to D
            self.fp.write(self._formatted_string('A=D', 'Save segment value to D'))
            self.fp.write(self._formatted_string('D=M'))

            # Push segment value to stack
            self._save_D_to_stack()
            self._increment_stack_pointer()

        def _pop_named_segment():
            if segment == 'pointer':
                address = 'THIS' if index == 0 else 'THAT'
                self.fp.write(self._formatted_string('@{}'.format(address), 'Save pointer address {} to D'.format(index)))
                self.fp.write(self._formatted_string('D=A'))
            else:
                address = segment_to_address[segment]
                self._set_D_to_segment_address(address, index, is_temp=(segment == 'temp'))

            # Save address to stack (above x)
            self._save_D_to_stack()
            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_D()

            # Set A to address (located at SP + 1)
            self.fp.write(self._formatted_string('@SP', 'Set A to address (located at @SP + 1)'))
            self.fp.write(self._formatted_string('A=M+1', '- location above @SP'))
            self.fp.write(self._formatted_string('A=M', '- value at location above @SP'))

            # Save D (popped value) to address (in segment)
            self.fp.write(self._formatted_string('M=D', 'Save D (popped value) to address (in segment)'))


        #
        # Method
        #
        segment_to_address = {
            'local': 'LCL',
            'argument': 'ARG',
            'this': 'THIS',
            'that': 'THAT',
            'temp': '5',
            'static': '16'
        }
        named_segments = ['local', 'argument', 'this', 'that', 'temp', 'pointer', 'static']
        # Call func & write call info
        self.fp.write("// ----- {} {} {} -----\n".format(commandType.name, segment, index))

        if commandType == CommandType.C_PUSH and segment == 'constant':
            _push_constant()
        elif commandType == CommandType.C_PUSH and segment in named_segments:
            _push_named_segment()
        elif commandType == CommandType.C_POP and segment in named_segments:
            _pop_named_segment()
        else:
            self.fp.write('// - NOT IMPLEMENTED: {} {} {}\n'.format(commandType.name, segment, index))


    #
    # BRANCHING
    #

    # TESTED
    def writeLabel(self, label: str):
        self.fp.write("// ----- LABEL -----\n")
        self.fp.write(self._formatted_string('({})'.format(label), 'Write label', indented=False))

    # TESTED
    def writeGoto(self, label: str):
        self.fp.write("// ----- GOTO -----\n")
        self.fp.write(self._formatted_string('@{}'.format(label), '- load jump address'))
        self.fp.write(self._formatted_string('0;JMP', '- unconditional jump'))

    # TESTED
    def writeIf(self, label: str):
        self.fp.write("// ----- IF-GOTO -----\n")
        self._decrement_stack_pointer()
        self._save_dereferenced_value_to_D()

        self.fp.write(self._formatted_string('@{}'.format(label), '- save jump location'))
        self.fp.write(self._formatted_string('D;JNE', '- jump if non-zero'))

    #
    # FUNCTIONS
    #

    # TESTED
    def writeFunction(self, functionName: str, nVars: int):

        # Set loop
        self.fp.write("// ----- Function {} {} -----\n".format(functionName, nVars))
        self.fp.write(self._formatted_string('({})'.format(functionName), 'Write function entry', indented=False))

        # Set LCL
        self.fp.write(self._formatted_string('@SP', 'Set LCL to SP'))
        self.fp.write(self._formatted_string('D=M'))
        self.fp.write(self._formatted_string('@LCL'))
        self.fp.write(self._formatted_string('M=D'))

        # Push 0 to LCL
        for i in range(nVars):
            self.fp.write(self._formatted_string('@SP', 'Push 0 to LCL (loop 0 of {})'.format(nVars)))
            self.fp.write(self._formatted_string('A=M'))
            self.fp.write(self._formatted_string('M=0'))
            self._increment_stack_pointer()

    # TODO
    def writeCall(self, functionName: str, nVars: int):
        def _save_pointer_from_frame(pointer: str):
            self.fp.write(self._formatted_string('@{}'.format(pointer), 'Get value of {} pointer'.format(pointer)))
            self.fp.write(self._formatted_string('D=M'))

            self._save_D_to_stack()
            self._increment_stack_pointer()

        self.fp.write("// ----- CALL {} {} -----\n".format(functionName, nVars))
        returnAddress = 'RETURN.{}'.format(self.return_counter)
        self.return_counter += 1

        # 1. push returnAddress
        self.fp.write(self._formatted_string(
            '@{}'.format(returnAddress),
            'Save the return address to D'
        ))
        self.fp.write(self._formatted_string('D=A'))
        self._save_D_to_stack()
        self._increment_stack_pointer()

        # 2. SAVE POINTERS
        _save_pointer_from_frame('LCL')
        _save_pointer_from_frame('ARG')
        _save_pointer_from_frame('THIS')
        _save_pointer_from_frame('THAT')

        # 3. Reposition ARG
        self.fp.write(self._formatted_string('@SP', 'Reposition ARG to (SP - 5 - nArgs)'))
        self.fp.write(self._formatted_string('A=M-1'))
        for i in range(4 + nVars):
            self.fp.write(self._formatted_string('A=A-1'))

        self.fp.write(self._formatted_string('D=A', '- Save address to D then set ARG to D'))
        self.fp.write(self._formatted_string('@ARG'))
        self.fp.write(self._formatted_string('M=D'))

        # 4. Reposition LCL
        self.fp.write(self._formatted_string('@SP', 'Set LCL to value of SP'))
        self.fp.write(self._formatted_string('D=M'))
        self.fp.write(self._formatted_string('@LCL'))
        self.fp.write(self._formatted_string('M=D'))

        # 5. Transfer control to callee
        self.fp.write(self._formatted_string('@{}'.format(functionName), 'Jump to callee'))
        self.fp.write(self._formatted_string('0;JMP'))

        # 6. Return address
        self.fp.write(self._formatted_string(
            '({})'.format(returnAddress),
            'Set the label for the function call return address',
            indented=False
        ))


    # TESTED - STUDY THIS
    def writeReturn(self):
        def _restore_pointer_from_frame(pointer: str):
            self.fp.write(self._formatted_string('@TEMP', 'Get {} from frame'.format(pointer)))
            self.fp.write(self._formatted_string('M=M-1'))
            self.fp.write(self._formatted_string('A=M'))

            self.fp.write(self._formatted_string('D=M', 'Restore {} value from frame'.format(pointer)))
            self.fp.write(self._formatted_string('@{}'.format(pointer)))
            self.fp.write(self._formatted_string('M=D'))

        self.fp.write("// ----- RETURN -----\n")

        # Save LCL to TEMP
        self.fp.write(self._formatted_string('@LCL', 'Save LCL to TEMP'))
        self.fp.write(self._formatted_string('D=M'))
        self.fp.write(self._formatted_string('@TEMP'))
        self.fp.write(self._formatted_string('M=D'))

        # Save Return address
        self.fp.write(self._formatted_string('@LCL', 'Get return address'))
        self.fp.write(self._formatted_string('A=M-1', '- return address = LCL - 5'))
        for i in range(4):
            self.fp.write(self._formatted_string('A=A-1'))
        self.fp.write(self._formatted_string('D=A'))

        self.fp.write(self._formatted_string('@TEMP', 'Save return address to TEMP + 1'))
        self.fp.write(self._formatted_string('A=A+1'))
        self.fp.write(self._formatted_string('M=D'))

        # 2. Save return val to ARG address
        # Retval
        self._decrement_stack_pointer()
        self._save_dereferenced_value_to_D()
        self.fp.write(self._formatted_string('@ARG', 'Save return value to ARG address'))
        self.fp.write(self._formatted_string('A=M'))
        self.fp.write(self._formatted_string('M=D'))

        # SP
        self.fp.write(self._formatted_string('@ARG', 'Reset @SP to @ARG + 1'))
        self.fp.write(self._formatted_string('D=M'))
        self.fp.write(self._formatted_string('@SP'))
        self.fp.write(self._formatted_string('M=D+1'))

        # 3. RESTORE POINTERS
        _restore_pointer_from_frame('THAT')
        _restore_pointer_from_frame('THIS')
        _restore_pointer_from_frame('ARG')
        _restore_pointer_from_frame('LCL')

        # 4. Jump to return address
        self.fp.write(self._formatted_string('@TEMP', 'Jump to return address (from TEMP + 1)'))
        self.fp.write(self._formatted_string('A=A+1'))
        self.fp.write(self._formatted_string('A=M'))
        self.fp.write(self._formatted_string('0;JMP'))


    #
    # HELPERS
    #

    def _formatted_string(self, instruction: str, comment: str = None, indented: bool = True) -> str:
        spacer = "\t" if indented else ""
        if comment != None and comment != "":
            return '{0}{1: <21} // {2}\n'.format(spacer, instruction, comment)
        else:
            return '{}{}'.format(spacer, instruction.strip() + '\n')

    def _set_D_to_segment_address(self, address, index, is_temp=False):
        self.fp.write(self._formatted_string('@{}'.format(address), 'Save segment address to D'))
        if is_temp:
            self.fp.write(self._formatted_string('D=A'))
        else:
            self.fp.write(self._formatted_string('D=M'))
        if index > 0:
            self.fp.write(self._formatted_string('@{}'.format(index), '- update D to [segment + index]'))
            self.fp.write(self._formatted_string('D=D+A'))

    def _save_D_to_stack(self):
        self.fp.write(self._formatted_string('@SP', 'Save D to the stack'))
        self.fp.write(self._formatted_string('A=M'))
        self.fp.write(self._formatted_string('M=D'))

    def _save_dereferenced_value_to_D(self):
        self.fp.write(self._formatted_string('@SP', 'Save the dereferenced value to D'))
        self.fp.write(self._formatted_string('A=M'))
        self.fp.write(self._formatted_string('D=M'))

    def _save_dereferenced_value_to_A(self, reload_stack: bool):
        # TODO: Clean this up
        # if reload_stack:
        self.fp.write(self._formatted_string('@SP', 'Save the dereferenced value to A'))
        self.fp.write(self._formatted_string('A=M', '- load pointer address'))
        self.fp.write(self._formatted_string('A=M', '- load pointer value'))
        # else:
        #     self.fp.write(self._formatted_string('A=M', 'Save the dereferenced value to A'))

    def _save_comparison_to_D(self, jump_code: str, description: str):
        # Get difference
        # [x, y] on stack --> D=y, A=x --> test A-D for x > y
        self.fp.write(self._formatted_string('D=A-D', description))

        # Load jump address
        self.fp.write(self._formatted_string(
            '@ARITHTRUE{}'.format(self.arithmetic_jump_counter),
            '- true jump location'
        ))
        self.fp.write(self._formatted_string('D;{}'.format(jump_code), '- jump if true'))

        # Handle false case
        self.fp.write(self._formatted_string('D=0', '- save false value'))

        # Unconditional jump (false case)
        self.fp.write(self._formatted_string(
            '@CONTINUE{}'.format(self.arithmetic_jump_counter),
            '- false jump location'
        ))
        self.fp.write(self._formatted_string('0;JMP', '- jump over true case'))

        # Handle true case
        self.fp.write(self._formatted_string(
            '(ARITHTRUE{})'.format(self.arithmetic_jump_counter),
            '- handle true case'
        ))
        self.fp.write(self._formatted_string('D=-1', '- save true value'))

        # Continue
        self.fp.write(self._formatted_string(
            '(CONTINUE{})'.format(self.arithmetic_jump_counter)
        ))

        self.arithmetic_jump_counter += 1

    def _decrement_stack_pointer(self):
        self.fp.write(self._formatted_string('@SP', 'Decrement the stack pointer'))
        self.fp.write(self._formatted_string('M=M-1'))

    def _increment_stack_pointer(self):
        self.fp.write(self._formatted_string('@SP', 'Increment the stack pointer'))
        self.fp.write(self._formatted_string('M=M+1'))


if __name__ == "__main__":
    print("Inside CodeWriter")
    with CodeWriter("./test.asm") as writer:
        # Arithmetic tests
        writer.writeArithmetic("add")
        writer.writeArithmetic("sub")
        writer.writeArithmetic("neg")
        writer.writeArithmetic("eq")
        writer.writeArithmetic("gt")
        writer.writeArithmetic("lt")
        writer.writeArithmetic("and")
        writer.writeArithmetic("or")
        writer.writeArithmetic("not")

        # Push pop tests
        writer.writePushPop(CommandType.C_PUSH, "constant", 4)
        writer.writePushPop(CommandType.C_PUSH, "local", 4)
        writer.writePushPop(CommandType.C_POP, "local", 2)

        # Branching tests

        # File tests

        # Function tests
