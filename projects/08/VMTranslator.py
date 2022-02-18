#!/usr/bin/env python
import sys
import os
from pathlib import Path
from Parser import Parser, CommandType
from CodeWriter import CodeWriter

'''
# TODO:
- Handle directories
    - Set filename for codewriter
    - Handle multiple parsers
'''

class VMTranslator:
    parser = None
    parsers = []
    codeWriter = None

    # TODO
    def __init__(self, input_path: str, output_path: str):
        if os.path.isdir(input_path):
            files = [
                os.path.join(input_path, filename)
                for filename in os.listdir(input_path)
                if filename.endswith('.vm')
            ]
            if output_path == None:
                directory = os.path.split(input_path)[-1]
                output_path = os.path.join(input_path, directory) + '.asm'
            self.parsers = [Parser(path) for path in files]
            self.codeWriter = CodeWriter(output_path)
        else:
            if output_path == None:
                filepath = os.path.splitext(input_path)[0]
                output_path = filepath + '.asm'
            self.parsers = [Parser(input_path)]
            self.codeWriter = CodeWriter(output_path)

    def translate(self):
        for parser in self.parsers:
            self._translate_parser(parser)

        self.codeWriter.close()

    def _translate_parser(self, parser):
        def _print_command_info(comment: str):
            print("> {0:<35}{1}".format(comment, parser.line))

        self.codeWriter.setFileName(parser.filename)
        while parser.hasMoreLines():
            parser.advance()
            command = parser.commandType()

            if command == CommandType.C_ARITHMETIC:
                _print_command_info("Writing Arithmetic Command: ")
                self.codeWriter.writeArithmetic(parser.line)

            elif command in [CommandType.C_PUSH, CommandType.C_POP]:
                _print_command_info("Writing Push Pop Command: ")
                arg1 = parser.arg1()
                arg2 = parser.arg2()
                self.codeWriter.writePushPop(command, arg1, arg2)

            elif command == CommandType.C_LABEL:
                _print_command_info("Writing Label Command: ")
                arg1 = parser.arg1()
                self.codeWriter.writeLabel(arg1)

            elif command == CommandType.C_GOTO:
                _print_command_info("Writing Goto Command: ")
                arg1 = parser.arg1()
                self.codeWriter.writeGoto(arg1)

            elif command == CommandType.C_IF:
                _print_command_info("Writing If-Goto Command: ")
                arg1 = parser.arg1()
                self.codeWriter.writeIf(arg1)

            elif command == CommandType.C_FUNCTION:
                _print_command_info("Writing Function Command: ")
                arg1 = parser.arg1()
                arg2 = parser.arg2()
                self.codeWriter.writeFunction(arg1, arg2)

            elif command == CommandType.C_RETURN:
                _print_command_info("Writing Return Command: ")
                self.codeWriter.writeReturn()

            elif command == CommandType.C_CALL:
                _print_command_info("Writing Call Command: ")
                arg1 = parser.arg1()
                arg2 = parser.arg2()
                self.codeWriter.writeCall(arg1, arg2)


def main():
    """
    Get the filename argument from command line args.
    Read the file contents and clean up lines by removing non-code strings.
    """
    # Make sure we have a filename argument
    if len(sys.argv) < 2:
        sys.exit("Expected filepath argument for input.")

    input_path = Path(sys.argv[1])
    output_path = None

    if len(sys.argv) == 3:
        output_path = Path(sys.argv[2])

    if(not input_path.exists()):
        sys.exit("Filepath does not exist.")

    # Assemble code
    translator = VMTranslator(input_path, output_path)
    translator.translate()

if __name__ == "__main__":
    main()
