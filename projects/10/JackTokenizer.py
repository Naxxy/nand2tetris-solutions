#!/usr/bin/env python3
from enum import Enum, IntEnum
from itertools import chain
from xml.sax import saxutils
import re

class TokenType(IntEnum):
    KEYWORD = 0,
    SYMBOL = 1,
    IDENTIFIER = 2,
    INT_CONST = 3,
    STRING_CONST = 4

    def tag(self) -> str:
        if self == TokenType.KEYWORD:
            tag = "keyword"
        elif self == TokenType.SYMBOL:
            tag = "symbol"
        elif self == TokenType.IDENTIFIER:
            tag = "identifier"
        elif self == TokenType.INT_CONST:
            tag = "integerConstant"
        elif self == TokenType.STRING_CONST:
            tag = "stringConstant"

        return tag

    def tagWithValue(self, value) -> str:
        if self == TokenType.KEYWORD:
            tag = "keyword"
            value = value.stringValue()
        elif self == TokenType.SYMBOL:
            tag = "symbol"
            value = saxutils.escape(value)
        elif self == TokenType.IDENTIFIER:
            tag = "identifier"
        elif self == TokenType.INT_CONST:
            tag = "integerConstant"
        elif self == TokenType.STRING_CONST:
            tag = "stringConstant"

        return "<{0}> {1} </{0}>".format(tag, value)

class Keyword(IntEnum):
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

    def stringValue(self):
        for (key, value) in Keyword.keywordMap().items():
            if value == self:
                return key

    def keywordMap():
        return {
            'class': 0,
            'method': 1,
            'function': 2,
            'constructor': 3,
            'int': 4,
            'boolean': 5,
            'char': 6,
            'void': 7,
            'var': 8,
            'static': 9,
            'field': 10,
            'let': 11,
            'do': 12,
            'if': 13,
            'else': 14,
            'while': 15,
            'return': 16,
            'true': 17,
            'false': 18,
            'null': 19,
            'this': 20
        }

    def keywordList():
        return list(Keyword.keywordMap().keys())

class JackTokenizer:
    fp = None
    tokens = None
    token_index = 0

    commentsRegex = re.compile(r".*(\/\/.*)|.*(\/\*\*.*\*\/)") # Assumes comments are one line only
    keywordRegex = re.compile('|'.join(['({})'.format(x) for x in Keyword.keywordList()]))
    symbolRegex = re.compile(r"^(\{|\}|\(|\)|\[|\]|\.|,|;|\+|-|\*|\/|&|\||<|>|=|~)")
    identifierRegex = re.compile(r"^([a-zA-Z][a-zA-Z0-9_]*)")
    stringValueRegex = re.compile(r"^\"(.*)\"")
    integerValueRegex = re.compile(r"^([0-9]+)")
    regexList = [
        keywordRegex,
        symbolRegex,
        identifierRegex,
        stringValueRegex,
        integerValueRegex
    ]

    def __init__(self, filepath, debug=False):
        if not debug:
            self.fp = open(filepath, 'r')
        self.tokens = None
        self.token_index = 0
        self.advance()

    def __del__(self):
        self.fp.close()

    def __enter__(self):
        # File already opened in initialiser
        return self

    def __exit__(self):
        self.fp.close()
        return

    # DONE
    def hasMoreTokens(self) -> bool:
        if not self.tokens or self.token_index < (len(self.tokens) - 1):
            return True

        # Need to check more lines
        tokens = []
        cursor_position = self.fp.tell()
        while not tokens:
            next_line = self.fp.readline()
            if next_line == "":
                return False
            tokens = self._tokensForLine(next_line)

        self.fp.seek(cursor_position)
        return True

    # DONE
    def advance(self):
        if not self.tokens:
            self.token_index = 0
            while not self.tokens:
                next_line = self.fp.readline()
                self.tokens = self._tokensForLine(next_line)
        elif self.token_index < (len(self.tokens) - 1):
            self.token_index += 1
        else:
            # Need to fetch next line
            self.tokens = []
            self.token_index = 0
            while not self.tokens:
                next_line = self.fp.readline()
                self.tokens = self._tokensForLine(next_line)

    # CHECK
    def peek(self):
        # Save state
        cursor_position = self.fp.tell()
        token_index = self.token_index
        tokens = self.tokens

        self.advance()

        # Get values
        type = self.tokenType()
        if type == TokenType.KEYWORD:
            value = self.keyWord()
        elif type == TokenType.SYMBOL:
            value = self.symbol()
        elif type == TokenType.IDENTIFIER:
            value = self.identifier()
        elif type == TokenType.INT_CONST:
            value = self.intVal()
        elif type == TokenType.STRING_CONST:
            value = self.stringVal()
        else:
            raise Exception("Invalid token type in peek")

        # Restore state
        self.fp.seek(cursor_position)
        self.token_index = token_index
        self.tokens = tokens

        print(self.tokens)
        return (type, value)


    # DONE
    def tokenType(self) -> TokenType:
        token = self.tokens[self.token_index]

        if self.keywordRegex.match(token):
            return TokenType.KEYWORD
        elif self.symbolRegex.match(token):
            return TokenType.SYMBOL
        elif self.identifierRegex.match(token):
            return TokenType.IDENTIFIER
        elif self.integerValueRegex.match(token):
            return TokenType.INT_CONST
        elif self.stringValueRegex.match(token):
            return TokenType.STRING_CONST

        raise Exception("TokenType is unknown for token \"{}\"".format(token))

    # DONE
    def keyWord(self) -> Keyword:
        map = Keyword.keywordMap()
        token = self.tokens[self.token_index]

        return Keyword(map[token])

    # DONE
    def symbol(self) -> chr:
        return str(self.tokens[self.token_index])

    # DONE
    def identifier(self) -> str:
        return str(self.tokens[self.token_index])

    # DONE
    def intVal(self) -> int:
        return int(self.tokens[self.token_index])

    # DONE
    def stringVal(self) -> str:
        return str(self.tokens[self.token_index])

    # DONE
    def _tokensForLine(self, line):
        # Strip comments
        matches = self.commentsRegex.match(line)
        if matches:
            comment = matches.group(0)
            line = self.commentsRegex.sub('', comment)
        if line.strip() == '' or line.strip() == '\n':
            return []

        original_line = line
        tokens = []
        while len(line):
            line = line.lstrip()

            token = None
            for regex in self.regexList:
                matches = regex.match(line)
                if matches:
                    token = matches.group(0)
                    line = regex.sub('', line, 1)
                    tokens.append(token)
                    break

            if not token:
                line = line[1:]

        return tokens


if __name__ == "__main__":
    tokenizer = JackTokenizer("ArrayTest/Main.jack", False)

    while(tokenizer.hasMoreTokens()):
        type = tokenizer.tokenType()
        if type == TokenType.KEYWORD:
            value = tokenizer.keyWord()
        elif type == TokenType.SYMBOL:
            value = tokenizer.symbol()
        elif type == TokenType.IDENTIFIER:
            value = tokenizer.identifier()
        elif type == TokenType.INT_CONST:
            value = tokenizer.intVal()
        elif type == TokenType.STRING_CONST:
            value = tokenizer.stringVal()
        else:
            value = None
        tokenizer.advance()

        print('{:40} - {:10}, {}'.format(type.tagWithValue(value), str(tokenizer.tokens), tokenizer.token_index))
