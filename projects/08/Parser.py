#!/usr/bin/env python

from enum import Enum
import sys
import os

class CommandType(Enum):
    C_ARITHMETIC = 0,
    C_PUSH = 1,
    C_POP = 2,
    C_LABEL = 3,
    C_GOTO = 4,
    C_IF = 5,
    C_FUNCTION = 6,
    C_RETURN = 7,
    C_CALL = 8


class Parser:
    fp = None
    filename = None
    line = None

    def __init__(self, filepath: str):
        self.fp = open(filepath, 'r')
        self.filename = os.path.split(filepath)[-1]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type != None or exc_value != None or traceback != None:
            print('Exiting context: ', self, exc_type, exc_value, traceback)

        self.fp.close()
        return True # suppress errors

    def hasMoreLines(self) -> bool:
        skip_line = True
        line = None
        has_more = False

        while skip_line:
            pos = self.fp.tell()
            line = self.fp.readline()

            if line.startswith("//") or line == '\n':
                continue
            elif line == None or line == '':
                skip_line = False
                has_more = False
            else:
                skip_line = False
                has_more = True
                self.fp.seek(pos)
        return has_more

    def advance(self):
        self.line = self.fp.readline()

        # Remove comments
        index = self.line.find("//")
        if index != -1:
            self.line = self.line[0:index]

        # clean newlines / whitespace
        self.line = self.line.strip()

    def commandType(self) -> CommandType:
        commandString = self.line.split()[0]

        if commandString in ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']:
            return CommandType.C_ARITHMETIC
        elif commandString == 'push':
            return CommandType.C_PUSH
        elif commandString == 'pop':
            return CommandType.C_POP
        elif commandString == 'label':
            return CommandType.C_LABEL
        elif commandString == 'if-goto':
            return CommandType.C_IF
        elif commandString == 'goto':
            return CommandType.C_GOTO
        elif commandString == 'function':
            return CommandType.C_FUNCTION
        elif commandString == 'return':
            return CommandType.C_RETURN
        elif commandString == 'call':
            return CommandType.C_CALL

    def arg1(self) -> str:
        arg = self.line.split()[1]
        return arg

    def arg2(self) -> int:
        arg = self.line.split()[2]
        return int(arg)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Expected filepath argument for input.")

    input_path = sys.argv[1]


    with Parser(input_path) as parser:
        while parser.hasMoreLines():
            parser.advance()
            parser.commandType()
