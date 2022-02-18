#! /usr/bin/env python

import sys
import os
from pathlib import Path
from pprint import pprint
from Parser import Parser, InstructionType
from Code import Code

class Assembler:
    parser = None
    code = None
    output_filepath = None

    def __init__(self, input_filepath: str, output_filepath: str):
        self.parser = Parser(input_filepath)
        self.code = Code()
        self.output_filepath = output_filepath

    # TODO
    def buildSymbolTable(self):
        pass

    def codeForLine(self) -> str:
        # C_INSTRUCTION
        if(self.parser.instructionType() == InstructionType.C_INSTRUCTION):
            d = self.parser.dest()
            c = self.parser.comp()
            j = self.parser.jump()

            code = "111"
            code += self.code.comp(c)
            code += self.code.dest(d)
            code += self.code.jump(j)
            print("[C] Code is: {} for line: {}".format(code, self.parser.current_line))
            return code

        # A_INSTRUCTION or L_INSTRUCTION
        elif(self.parser.instructionType() == InstructionType.A_INSTRUCTION):
            # Get the symbol
            value = self.parser.symbol()

            # Get the address from the symbol
            if value.isnumeric():
                value = int(value)
            elif self.parser.symbol_table.contains(value):
                value = self.parser.symbol_table.getAddress(value)
            else:
                self.parser.symbol_table.addVariable(value)
                value = self.parser.symbol_table.getAddress(value)

            # Convert the address to binary
            binary = format(value, 'b').rjust(16, '0')
            print("[A] Code is: {} for line: {}".format(binary, self.parser.current_line))
            return binary


    def assembleCode(self):
        with open(self.output_filepath, 'w') as fp:

            # Process each line in the parser
            self.parser.buildLabels()
            while self.parser.hasMoreLines():
                self.parser.advance()

                # Skip L-Instructions
                if self.parser.instructionType() == InstructionType.L_INSTRUCTION:
                    continue

                # Get the line
                line = self.codeForLine()

                fp.write(line + '\n')


def main():
    """
    Get the filename argument from command line args.
    Read the file contents and clean up lines by removing non-code strings.
    """
    # Make sure we have a filename argument
    if len(sys.argv) < 2:
        sys.exit("Expected filepath argument for input.")

    input_path = Path(sys.argv[1])
    output_path = input_path.with_suffix(".hack")

    if len(sys.argv) == 3:
        output_path = Path(sys.argv[2])

    if(not input_path.exists()):
        sys.exit("Filepath does not exist.")

    if(not input_path.is_file()):
        sys.exit("Path argument is not a file.")

    # Assemble code
    assembler = Assembler(str(input_path), str(output_path))
    assembler.buildSymbolTable()
    assembler.assembleCode()


if __name__ == "__main__":
    main()
