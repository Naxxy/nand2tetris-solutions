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

# DONE FOR NOW
class Parser:
    fp = None
    line = None

    # DONE
    def __init__(self, filename: str):
        self.fp = open(filename, 'r')

    # DONE
    def __enter__(self):
        return self

    # DONE
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type != None or exc_value != None or traceback != None:
            print('Exiting context: ', self, exc_type, exc_value, traceback)

        self.fp.close()
        return True # suppress errors

    # DONE
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

    # DONE
    def advance(self):
        self.line = self.fp.readline()

        # Remove comments
        index = self.line.find("//")
        if index != -1:
            self.line = self.line[0:index]

        # clean newlines / whitespace
        self.line = self.line.strip()

    # DONE FOR NOW
    def commandType(self) -> CommandType:
        commandType = self.line.split()[0]

        if commandType in ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']:
            return CommandType.C_ARITHMETIC
        elif commandType == 'push':
            return CommandType.C_PUSH
        elif commandType == 'pop':
            return CommandType.C_POP

        # --- TODO ---
        # elif commandType == CommandType.C_LABEL:
        #     pass
        # elif commandType == CommandType.C_GOTO:
        #     pass
        # elif commandType == CommandType.C_IF:
        #     pass
        # elif commandType == CommandType.C_FUNCTION:
        #     pass
        # elif commandType == CommandType.C_RETURN:
        #     pass
        # elif commandType == CommandType.C_CALL:
        #     pass

    # DONE
    def arg1(self) -> str:
        arg = self.line.split()[1]
        return arg

    # DONE
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
