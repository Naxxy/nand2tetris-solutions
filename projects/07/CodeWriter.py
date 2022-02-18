#!/usr/bin/env python
from Parser import CommandType

# TODO
class CodeWriter:
    fp = None
    arithmetic_jump_counter = 0

    def __init__(self, filename: str):
        self.fp = open(filename, 'w')
        self.arithmetic_jump_counter = 0

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

    def writeArithmetic(self, command: str):
        # NOTE: True mapped to -1, False mapped to 0
        def _add(): # TESTED
            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_D()

            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_A(False)

            self.fp.write(self._formatted_string('D=A+D', 'Perform the addition'))

            self._save_D_to_stack()
            self._increment_stack_pointer()

        def _sub(): # TESTED
            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_D()

            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_A(False)

            self.fp.write(self._formatted_string('D=A-D', 'Perform the subtraction'))

            self._save_D_to_stack()
            self._increment_stack_pointer()

        def _neg(): # TESTED
            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_D()

            self.fp.write(self._formatted_string('D=-D', 'Perform the negation'))

            self._save_D_to_stack()
            self._increment_stack_pointer()

        def _eq(): # TESTED
            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_D()

            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_A(False)

            self._save_comparison_to_D('JEQ', 'Check equality')

            self._save_D_to_stack()
            self._increment_stack_pointer()

        def _gt(): # TESTED
            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_D()

            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_A(False)

            self._save_comparison_to_D('JGT', 'Check greater than')

            self._save_D_to_stack()
            self._increment_stack_pointer()

        def _lt(): # TESTED?
            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_D()

            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_A(False)

            self._save_comparison_to_D('JLT', 'Check less than')

            self._save_D_to_stack()
            self._increment_stack_pointer()

        def _and(): # TESTED
            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_D()

            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_A(False)

            self.fp.write(self._formatted_string('D=A&D', 'Perform the bit-wise AND'))

            self._save_D_to_stack()
            self._increment_stack_pointer()

        def _or(): # TESTED
            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_D()

            self._decrement_stack_pointer()
            self._save_dereferenced_value_to_A(False)

            self.fp.write(self._formatted_string('D=A|D', 'Perform the bit-wise OR'))

            self._save_D_to_stack()
            self._increment_stack_pointer()

        def _not(): # TESTED
            self._decrement_stack_pointer()
            self.fp.write(self._formatted_string('@SP', 'Save the dereferenced value to D'))
            self.fp.write(self._formatted_string('A=M'))
            self.fp.write(self._formatted_string('D=!M', 'Perform the bit-wise NOT'))

            self._save_D_to_stack()
            self._increment_stack_pointer()


        switcher = {
            'add': _add,
            'sub': _sub,
            'neg': _neg,
            'eq': _eq,
            'gt': _gt,
            'lt': _lt,
            'and': _and,
            'or': _or,
            'not': _not
        }

        func = switcher.get(command, None)
        if func:
            # Write section comment
            self.fp.write("// ----- {} -----\n".format(command.upper()))
            func()

    # TODO
    def writePushPop(self, commandType: CommandType, segment: str, index: int):
        def _push_constant(): # TESTED
            # Load value
            self.fp.write(self._formatted_string('@{}'.format(index), 'Save value to top of stack'))
            self.fp.write(self._formatted_string('D=A', '- save literal to D'))

            # Save value
            self._save_D_to_stack()
            self._increment_stack_pointer()

        def _push_named_segment(): # TESTED
            # Get segment address
            if segment == 'pointer':
                address = 'THIS' if index == 0 else 'THAT'
                self.fp.write(self._formatted_string('@{}'.format(address), 'Save pointer address {} to D'.format(index)))
                self.fp.write(self._formatted_string('D=A'))
            else:
                address = segment_to_address[segment]
                self._set_D_to_segment_address(address, index)

            # Save segment to D
            self.fp.write(self._formatted_string('A=D', 'Save segment value to D'))
            self.fp.write(self._formatted_string('D=M'))

            # Push segment value to stack
            self._save_D_to_stack()
            self._increment_stack_pointer()

        def _pop_named_segment(): # TESTED
            if segment == 'pointer':
                address = 'THIS' if index == 0 else 'THAT'
                self.fp.write(self._formatted_string('@{}'.format(address), 'Save pointer address {} to D'.format(index)))
                self.fp.write(self._formatted_string('D=A'))
            else:
                address = segment_to_address[segment]
                self._set_D_to_segment_address(address, index)

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

        push_switcher = {
            'constant': _push_constant,
            'local': _push_named_segment,
            'argument': _push_named_segment,
            'this': _push_named_segment,
            'that': _push_named_segment,
            'temp': _push_named_segment,
            'pointer': _push_named_segment,
            'static': _push_named_segment
        }
        pop_switcher = {
            'local': _pop_named_segment,
            'argument': _pop_named_segment,
            'this': _pop_named_segment,
            'that': _pop_named_segment,
            'temp': _pop_named_segment,
            'pointer': _pop_named_segment,
            'static': _pop_named_segment
        }

        # Get the func to call
        if commandType == CommandType.C_PUSH:
            func = push_switcher.get(segment, None)
        else:
            func = pop_switcher.get(segment, None)

        # Call func & write call info
        if func:
            self.fp.write("// ----- {} {} {} -----\n".format(commandType.name, segment, index))
            func()
        else:
            self.fp.write('// - NOT IMPLEMENTED: {} {} {}\n'.format(commandType.name, segment, index))

    # DONE
    def close(self):
        self.fp.write(self._formatted_string('(INFINITE_LOOP)', 'Infinite Loop'))
        self.fp.write(self._formatted_string('@INFINITE_LOOP'))
        self.fp.write(self._formatted_string('0;JMP'))

        self.fp.close()

    #
    # HELPERS
    #

    def _formatted_string(self, instruction: str, comment: str = None) -> str:
        if comment != None and comment != "":
            return '{0: <21} // {1}\n'.format(instruction, comment)
        else:
            return instruction.strip() + '\n'

    def _set_D_to_segment_address(self, address, index):
        self.fp.write(self._formatted_string('@{}'.format(address), 'Save segment address to D'))
        self.fp.write(self._formatted_string('D=M'))
        if index > 0:
            self.fp.write(self._formatted_string('@{}'.format(index), '- update D to [segment + index]'))
            self.fp.write(self._formatted_string('D=D+A'))

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

    def _save_D_to_stack(self):
        self.fp.write(self._formatted_string('@SP', 'Save the result on the stack (overwrites arg)'))
        self.fp.write(self._formatted_string('A=M'))
        self.fp.write(self._formatted_string('M=D'))

    def _decrement_stack_pointer(self):
        self.fp.write(self._formatted_string('@SP', 'Decrement the stack pointer'))
        self.fp.write(self._formatted_string('M=M-1'))

    def _increment_stack_pointer(self):
        self.fp.write(self._formatted_string('@SP', 'Increment the stack pointer'))
        self.fp.write(self._formatted_string('M=M+1'))

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
