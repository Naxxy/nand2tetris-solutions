#!/usr/bin/env python
from enum import Enum

class TokenType(Enum):
    KEYWORD = 0,
    SYMBOL = 1,
    IDENTIFIER = 2,
    INT_CONST = 3,
    STRING_CONST = 4

    def tagWithValue(self, value) -> str:
        if self == TokenType.KEYWORD: tag = "keyword"
        elif self == TokenType.SYMBOL: tag = "symbol"
        elif self == TokenType.IDENTIFIER: tag = "identifier"
        elif self == TokenType.INT_CONST: tag = "integerConstant"
        elif self == TokenType.STRING_CONST: tag = "stringConstant"

        return "<{0}>{1}</{0}>".format(tag, value)

class Keyword(Enum):
    CLASS = 0,
    METHOD = 1,
    FUNCTION = 2,
    CONSTRUCTOR = 3,
    INT = 4,
    BOOLEAN = 5,
    CHAR = 6,
    VOID = 7,
    VAR = 8,
    STATIC = 9,
    FIELD = 10,
    LET = 11,
    DO = 12,
    IF = 13,
    ELSE = 14,
    WHILE = 15,
    RETURN = 16,
    TRUE = 17,
    FALSE = 18,
    NULL = 19,
    THIS = 20

class JackTokenizer:
    fp = None
    line = None
    token = None
    keywordList = [
        'class', 'constructor', 'function', 'method', 'field', 'static',
        'var', 'int', 'char', 'boolean', 'void', 'true', 'false',
        'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return'
    ]
    symbolList = [
        '{', '}', '(', ')', '[', ']', '.', ',', ';',
        '+', '-', '*', '/', '&', '|', '<', '>', '=', '~'
    ]

    def __init__(self, filepath, debug=False):
        if not debug:
            self.fp = open(filepath, 'r')
        self.line = None
        self.token = None

    # TODO
    def hasMoreTokens(self) -> bool:
        # cursor_position = self.fp.tell()
        #
        # # Beginning of file
        # if(self.token == None or self.line == None):
        #     self.line = self.fp.readline()
        #     self.token = self.line.split()[0]
        #
        # # Skip comments
        #
        #
        #
        #
        # print("Line is: \"{}\"".format(self.line.strip()))
        return False #self.line != ""

    # TODO
    def advance(self):
    pass

    # TODO
    def tokenType(self) -> TokenType:
        return TokenType.KEYWORD

    # TODO
    def keyWord(self) -> Keyword:
        return Keyword.NULL

    # TODO
    def symbol(self) -> chr:
        return "?"

    # TODO
    def identifier(self) -> str:
        return "TODO - IDENTIFIER"

    # TODO
    def intVal(self) -> int:
        return -1

    # TODO
    def stringVal(self) -> str:
        return "TODO - STRING VAL"

if __name__ == "__main__":
    print("Inside JackTokenizer")
