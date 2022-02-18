#!/usr/bin/env python
import sys
import os
from pathlib import Path
from Parser import Parser, CommandType
from CodeWriter import CodeWriter

class VMTranslator:
    parser = None
    codeWriter = None

    def __init__(self, input_path: str, output_path: str):
        self.parser = Parser(input_path)
        self.codeWriter = CodeWriter(output_path)

    def translate(self):
        while self.parser.hasMoreLines():
            self.parser.advance()
            command = self.parser.commandType()
            if command == CommandType.C_ARITHMETIC:
                print("> Writing Arithmetic Command: {}".format(self.parser.line))
                self.codeWriter.writeArithmetic(self.parser.line)
            elif command in [CommandType.C_PUSH, CommandType.C_POP]:
                arg1 = self.parser.arg1()
                arg2 = self.parser.arg2()
                print("> Writing Push Pop Command: {}".format(self.parser.line))
                self.codeWriter.writePushPop(command, arg1, arg2)
        self.codeWriter.close()



def main():
    """
    Get the filename argument from command line args.
    Read the file contents and clean up lines by removing non-code strings.
    """
    # Make sure we have a filename argument
    if len(sys.argv) < 2:
        sys.exit("Expected filepath argument for input.")

    input_path = Path(sys.argv[1])
    output_path = input_path.with_suffix(".asm")

    if len(sys.argv) == 3:
        output_path = Path(sys.argv[2])

    if(not input_path.exists()):
        sys.exit("Filepath does not exist.")

    if(not input_path.is_file()):
        sys.exit("Path argument is not a file.")

    # Assemble code
    translator = VMTranslator(input_path, output_path)
    translator.translate()

if __name__ == "__main__":
    main()
