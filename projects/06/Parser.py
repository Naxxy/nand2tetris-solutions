from enum import Enum
from pprint import pprint

test_code = [
    "@R0",              # 0
    "D=M",              # 1
    "@R1",              # 2
    "D=D-M",            # 3
    "@OUTPUT_FIRST",    # 4
    "D;JGT",            # 5
    "@R1",              # 6
    "D=M",              # 7
    "@OUTPUT_D",        # 8
    "0;JMP",            # 9
    "(OUTPUT_FIRST)",   # address 10
    "@R0",              # 10
    "D=M",              # 11
    "(OUTPUT_D)",       # address 12
    "@R2",              # 12
    "M=D",              # 13
    "(INFINITE_LOOP)",  # address 14
    "@INFINITE_LOOP",   # 14
    "0;JMP"             # 15
]

 # '@2',       # 0 - 0
 # 'D=A;JNE',  # 1 - 1
 # '@3',       # 2 - 2
 # 'D=D+A',    # 3 - 3
 # '(LOOP)',   # 4 - 4
 # '@0',       # 5 - 4
 # 'M=D',      # 6 - 5
 # '0;JMP'     # 7 - 6
#
# test_code = [
#     "@0",
#     "D=M",
#     "@1",
#     "D=D-M",
#     "@10",
#     "D;JGT",
#     "@1",
#     "D=M",
#     "@12",
#     "0;JMP",
#     "@0",
#     "D=M",
#     "@2",
#     "M=D",
#     "@14",
#     "0;JMP"
# ]

#
# TODO
#
# - Replace in-memory file with file pointer
# - Change "advance" method
# - Change "hasMoreLines" method

class InstructionType(Enum):
    A_INSTRUCTION = 1,
    C_INSTRUCTION = 2,
    L_INSTRUCTION = 3


class SymbolTable:
    symbols = {}
    variable_count = 0
    VARIABLE_INDEX_START = 16   # Variable mapping starts at RAM[16]

    def __init__(self):
        self.symbols = {
            "R0": 0,
            "R1": 1,
            "R2": 2,
            "R3": 3,
            "R4": 4,
            "R5": 5,
            "R6": 6,
            "R7": 7,
            "R8": 8,
            "R9": 9,
            "R10": 10,
            "R11": 11,
            "R12": 12,
            "R13": 13,
            "R14": 14,
            "R15": 15,

            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,

            "SCREEN": 16384,
            "KBD": 24576
        }

    def addVariable(self, symbol: str):
        self.symbols[symbol] = self.VARIABLE_INDEX_START + self.variable_count
        self.variable_count += 1

    def addEntry(self, symbol: str, address: int):
        self.symbols[symbol] = address

    def contains(self, symbol: str) -> bool:
        return symbol in self.symbols.keys()

    def getAddress(self, symbol: str) -> int:
        return self.symbols[symbol]


class Parser:
    filtered_lines = []
    symbol_table = None
    current_line = None
    line_number = -1
    index = -1

    # def __init__(self):
    #     self.filtered_lines = test_code
    #     self.symbol_table = SymbolTable()

    # DONE
    def __init__(self, filepath: str):
        """
        Reads the contents of the file, cleans the lines, and saves it as filtered_lines.
        """
        def clean_lines(lines: list) -> list:

            clean_lines = []
            # Remove comments lines & empty lines
            lines = [
                line.strip('\n') for line in lines
                if(not line.startswith("//") and line != "\n")
            ]

            # Remove trailing comments & whitespace
            for line in lines:
                if line == "\n":
                    # Remove empty lines
                    continue
                elif line.startswith("//"):
                    # Remove comment lines
                    continue
                elif "//" in line:
                    index = line.find("//")
                    line = line[0:index]
                    # Remove trailing comments

                # Remove leading & trailing whitespace
                line = line.lstrip(" ")
                line = line.rstrip(" ")
                clean_lines += [line]

            return clean_lines


        # Read file
        print("Opening file {}".format(filepath))
        with open(filepath) as fp:
            lines = fp.readlines()

        self.filtered_lines = clean_lines(lines)
        self.symbol_table = SymbolTable()

    # TODO
    def buildLabels(self):
        # Check all code
        while self.hasMoreLines():
            self.advance()
            if self.instructionType() == InstructionType.L_INSTRUCTION:
                symbol = self.symbol()
                address = self.line_number
                self.symbol_table.addEntry(symbol, address)

        # Reset code pointer
        self.current_line = None
        self.line_number = -1
        self.index = -1
        pprint(self.symbol_table.symbols)

    # DONE
    def hasMoreLines(self) -> bool:
        return self.index < len(self.filtered_lines) - 1

    # DONE
    def advance(self) -> None:
        # Increment line number iff previous instruction wasn't label
        if self.instructionType() != InstructionType.L_INSTRUCTION:
            self.line_number += 1

        # Get next line of code
        self.index += 1
        self.current_line = self.filtered_lines[self.index]

    # DONE
    def instructionType(self) -> InstructionType:
        """
        Returns the instruction type for the line at index
        """
        line = self.filtered_lines[self.index]

        if line.startswith("@"):
            return InstructionType.A_INSTRUCTION
        elif line.startswith("("):
            return InstructionType.L_INSTRUCTION
        else:
            return InstructionType.C_INSTRUCTION

    # DONE
    def symbol(self) -> str:
        """
        If the current instruction is (xxx), returns the symbol xxx. If the
        current instruction is @xxx, returns the symbol or decimal xxx (as a
        string).
        Should be called only if instructionType is A_INSTRUCTION or
        L_INSTRUCTION
        """
        if self.instructionType() == InstructionType.A_INSTRUCTION:
            return self.current_line.lstrip('@')
        elif self.instructionType() == InstructionType.L_INSTRUCTION:
            return self.current_line.lstrip('(').rstrip(')')

    # DONE
    def dest(self) -> str:
        """
        Returns the symbolic dest part of the current C-instruction (8 possibilities).
        Should be called only if instructionType is C INSTRUCTION.
        """
        index = self.current_line.find("=")
        if index == -1:
            return ""

        line = self.current_line[:index]
        return line

    # DONE
    def comp(self) -> str:
        """
        Returns the symbolic comp part of the current C-instruction (28 possibilities).
        Should be called only if instructionType is C INSTRUCTION.
        """

        line = self.current_line
        index = line.find(";")
        if index != -1:
            line = line[:index]

        index = line.find("=")
        if index != -1:
            line = line[index+1:]

        return line

    # DONE
    def jump(self) -> str:
        """
        Returns the symbolic comp part of the current C-instruction (28 possibilities).
        Should be called only if instructionType is C INSTRUCTION.
        """
        index = self.current_line.find(";")
        if index == -1:
            return ""

        line = self.current_line[index+1:]
        return line



if __name__ == "__main__":
    parser = Parser()
    parser.buildLabels()
    while parser.hasMoreLines():
        parser.advance()
        if parser.instructionType() == InstructionType.C_INSTRUCTION:
            print("\t{}-{} - {:12}{:8}{:8}{:8}".format(
                parser.index,
                parser.line_number,
                parser.current_line,
                parser.dest(),
                parser.comp(),
                parser.jump()
            ))
        else:
            print("\t{}-{} - {:12}{:8}{:20}".format(
                parser.index,
                parser.line_number,
                parser.current_line,
                parser.symbol(),
                parser.instructionType()
            ))
