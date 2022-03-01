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
    pass

if __name__ == "__main__":
    print("Inside JackTokenizer")
