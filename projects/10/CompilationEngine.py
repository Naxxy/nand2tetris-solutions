#!/usr/bin/env python

from JackTokenizer import JackTokenizer, Keyword, TokenType
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree
from xml.sax import saxutils
from xml.dom import minidom
from FileData import FileData

class CompilationEngine:
    fp_in = None
    tokenizer = None
    file_data = None
    operators = ['+', '-', '*', '/', '&', '|', '<', '>', '=']
    unary_operators = ['-', '~']
    keyword_constants = [Keyword.TRUE, Keyword.FALSE, Keyword.NULL, Keyword.THIS]

    def __init__(self, file_data: FileData, write_comments = False):
        self.tokenizer = JackTokenizer(file_data.input_path())
        self.fp_in = open(file_data.input_path(), 'r')
        self.file_data = file_data
        self.write_comments = write_comments
        self.compileClass()

    def __del__(self):
        self.fp_in.close()

    def __enter__(self):
        # File already opened in initialiser
        return self

    def __exit__(self):
        self.fp_in.close()
        return

    #################
    # CLASS METHODS #
    #################

    # DONE
    def compileClass(self):
        root = Element("class")
        print("COMPILE CLASS")
        if self.write_comments:
            root.append(Comment('COMPILE CLASS'))

        child = self._addKeyword(root, True)          # Class
        child = self._addIdentifier(root, True)       # ClassName
        child = self._addSymbol(root, True)           # {

        type = TokenType.KEYWORD
        while type == TokenType.KEYWORD:
            value = self.tokenizer.keyWord()
            if value in [Keyword.CONSTRUCTOR, Keyword.FUNCTION, Keyword.METHOD]:
                self.compileSubroutine(root)
            elif value in [Keyword.STATIC, Keyword.FIELD]:
                self.compileClassVarDec(root)

            type = self.tokenizer.tokenType()

        child = self._addSymbol(root, True)           # }

        with open(self.file_data.output_path(), 'w') as fp:
            fp.write(self._prettify(root))

    # DONE
    def compileClassVarDec(self, parent):
        print("COMPILE CLASS VARIABLE DECLARATION")
        if self.write_comments:
            parent.append(Comment('COMPILE CLASS VARIABLE DECLARATION'))
        node = SubElement(parent, 'classVarDec')

        self._addKeyword(node, True)                  # (static | field)
        if self.tokenizer.tokenType() == TokenType.IDENTIFIER:
            self._addIdentifier(node, True)           # className
        else:
            self._addKeyword(node, True)              # (int | boolean | char)

        self._addIdentifier(node, True)               # varName
        value = self._tokenizerValue(raw=True)
        while value != ';':
            self._addSymbol(node, True)               # ','
            self._addIdentifier(node, True)           # varName
            value = self._tokenizerValue(raw=True)

        self._addSymbol(node, True)                   # ';'

        return node

    # DONE
    def compileSubroutine(self, parent):
        print("COMPILE SUBROUTINE")
        if self.write_comments:
            parent.append(Comment('COMPILE SUBROUTINE'))
        node = SubElement(parent, 'subroutineDec')

        self._addKeyword(node, True)                # (constructor | function | method)
        type = self.tokenizer.tokenType()           # type = (int | char | boolean | className)
        if type == TokenType.IDENTIFIER:
            self._addIdentifier(node, True)         # className
        else:
            self._addKeyword(node, True)            # (void | int | char | boolean | className)

        self._addIdentifier(node, True)             # subroutineName
        self._addSymbol(node, True)                 # (
        self.compileParameterList(node)             # parameterList
        self._addSymbol(node, True)                 # )
        self.compileSubroutineBody(node)            # subroutineBody

        return node

    # DONE
    def compileParameterList(self, parent):
        print("COMPILE PARAMETER LIST")
        if self.write_comments:
            parent.append(Comment('COMPILE PARAMETER LIST'))
        node = SubElement(parent, 'parameterList')

        value = self._tokenizerValue()
        while value != ')':
            # Check the type
            type = self.tokenizer.tokenType()

            # Process the type
            if type == TokenType.KEYWORD:               # (int | char | boolean)
                self._addKeyword(node, True)
            elif type == TokenType.IDENTIFIER:          # (className | varName)
                self._addIdentifier(node, True)
            elif type == TokenType.SYMBOL:              # ','
                assert self.tokenizer.symbol() == ','
                self._addSymbol(node, True)
            else:
                raise Exception("Invalid token type: {}".format(type))

            # Advance
            type = self.tokenizer.tokenType()
            value = self._tokenizerValue()

        return node

    # DONE
    def compileSubroutineBody(self, parent):
        print("COMPILE SUBROUTINE BODY")
        if self.write_comments:
            parent.append(Comment('COMPILE SUBROUTINE BODY'))
        node = SubElement(parent, 'subroutineBody')

        self._addSymbol(node, True)                         # {
        while True:
            value = self._tokenizerValue(raw=True)
            if value == Keyword.VAR:
                self.compileVarDec(node)                    # varDec*
            elif value == '}':
                self._addSymbol(node, True)                 # }
                break
            else:
                self.compileStatements(node)                # statements

        return node

    # DONE
    def compileVarDec(self, parent):
        print("COMPILE VARIABLE DECLARATION")
        if self.write_comments:
            parent.append(Comment('COMPILE VARIABLE DECLARATION'))
        node = SubElement(parent, 'varDec')

        self._addKeyword(node, True)                  # var
        if self.tokenizer.tokenType() == TokenType.IDENTIFIER:
            self._addIdentifier(node, True)           # className
        else:
            self._addKeyword(node, True)              # (int | boolean | char)

        self._addIdentifier(node, True)               # varName
        value = self._tokenizerValue(raw=True)
        while value != ';':
            self._addSymbol(node, True)               # ','
            self._addIdentifier(node, True)           # varName
            value = self._tokenizerValue(raw=True)

        self._addSymbol(node, True)                   # ';'

        return node

    # DONE
    def compileStatements(self, parent):
        print("COMPILE STATEMENTS")
        if self.write_comments:
            parent.append(Comment('COMPILE STATEMENTS'))
        node = SubElement(parent, 'statements')

        while True:
            type = self.tokenizer.tokenType()
            if type != TokenType.KEYWORD:
                break

            value = self.tokenizer.keyWord()
            if value == Keyword.LET:
                self.compileLet(node)
            elif value == Keyword.IF:
                self.compileIf(node)
            elif value == Keyword.WHILE:
                self.compileWhile(node)
            elif value == Keyword.DO:
                self.compileDo(node)
            elif value == Keyword.RETURN:
                self.compileReturn(node)
            else:
                break

        return node

    # DONE
    def compileLet(self, parent):
        print("COMPILE LET")
        if self.write_comments:
            parent.append(Comment('COMPILE LET'))
        node = SubElement(parent, 'letStatement')

        self._addKeyword(node, True)                    # let
        self._addIdentifier(node, True)                 # varName
        if self._tokenizerValue() == '[':               # [ expression ]
            self._addSymbol(node, True)
            self.compileExpression(node)
            self._addSymbol(node, True)
        self._addSymbol(node, True)                     # '='
        self.compileExpression(node)                    # expression

        self._addSymbol(node, True)                     # ';'

        return node

    # DONE
    def compileIf(self, parent):
        print("COMPILE IF")
        if self.write_comments:
            parent.append(Comment('COMPILE IF'))
        node = SubElement(parent, 'ifStatement')

        self._addKeyword(node, True)            # if
        self._addSymbol(node, True)             # '('
        self.compileExpression(node)            # expression
        self._addSymbol(node, True)             # ')'
        self._addSymbol(node, True)             # '{'
        self.compileStatements(node)            # statements
        self._addSymbol(node, True)             # '}'
        if self._tokenizerValue(raw=True) == Keyword.ELSE:
                self._addKeyword(node, True)            # else
                self._addSymbol(node, True)             # '{'
                self.compileStatements(node)            # statements
                self._addSymbol(node, True)             # '}'

        return node

    # DONE
    def compileWhile(self, parent):
        print("COMPILE WHILE")
        if self.write_comments:
            parent.append(Comment('COMPILE WHILE'))
        node = SubElement(parent, 'whileStatement')

        self._addKeyword(node, True)            # while
        self._addSymbol(node, True)             # '('
        self.compileExpression(node)            # expression
        self._addSymbol(node, True)             # ')'
        self._addSymbol(node, True)             # '{'
        self.compileStatements(node)            # statements
        self._addSymbol(node, True)             # '}'
        return node

    # DONE
    def compileDo(self, parent):
        print("COMPILE DO")
        if self.write_comments:
            parent.append(Comment('COMPILE DO'))
        node = SubElement(parent, 'doStatement')

        self._addKeyword(node, True)            # do
        self._addSubroutineCall(node)            # expression
        self._addSymbol(node, True)             # ';'

        return node

    # DONE
    def compileReturn(self, parent):
        print("COMPILE RETURN")
        if self.write_comments:
            parent.append(Comment('COMPILE RETURN'))
        node = SubElement(parent, 'returnStatement')

        self._addKeyword(node, True)            # return
        if self._tokenizerValue() != ';':       # expression
            self.compileExpression(node)
        self._addSymbol(node, True)             # ';'

        return node

    # DONE
    def compileExpression(self, parent):
        print("COMPILE EXPRESSION")
        if self.write_comments:
            parent.append(Comment('COMPILE EXPRESSION'))
        node = SubElement(parent, 'expression')

        self.compileTerm(node)                  # term
        while self._tokenizerValue() in self.operators:
            self._addSymbol(node, True)         # op
            self.compileTerm(node)              # term

        return node

    # DONE
    def compileTerm(self, parent):
        print("COMPILE TERM")
        if self.write_comments:
            parent.append(Comment('COMPILE TERM'))
        node = SubElement(parent, 'term')

        type = self.tokenizer.tokenType()
        value = self._tokenizerValue(raw=True)
        if type == TokenType.INT_CONST:
            self.compileIntegerConstant(node)       # integerConstant
        elif type == TokenType.STRING_CONST:
            self.compileStringConstant(node)        # stringConstant
        elif value in self.keyword_constants:       # keywordConstant
            self._addKeyword(node, True)
        elif value in self.unary_operators:         # unaryOp term
            self._addSymbol(node, True)
            self.compileTerm(node)
        elif value == '(':                          # ( expression )
            self._addSymbol(node, True)
            self.compileExpression(node)
            self._addSymbol(node, True)
        elif type == TokenType.IDENTIFIER:
            (type, value) = self.tokenizer.peek()
            if value == '[':                        # varName [ expression ]
                self._addIdentifier(node, True)
                self._addSymbol(node, True)
                self.compileExpression(node)
                self._addSymbol(node, True)
            elif value in ['(', '.']:               # subroutineCall
                self._addSubroutineCall(node)
            else:
                self._addIdentifier(node, True)     # varName
        else:
            node.append(Comment(f'ILLEGAL CASE! \"{self.tokenizer.tokenType().tag()}\" - \"{self._tokenizerValue()}\"'))

        return node

    # DONE
    def compileExpressionList(self, parent):
        print("COMPILE EXPRESSION LIST")
        if self.write_comments:
            parent.append(Comment('COMPILE EXPRESSION LIST'))
        node = SubElement(parent, 'expressionList')

        type = self.tokenizer.tokenType()
        value = self._tokenizerValue()
        integerConstant = type == TokenType.INT_CONST
        stringConstant = type == TokenType.STRING_CONST
        keywordConstant = value in self.keyword_constants
        unaryOpCondition = value in self.unary_operators
        expressionCondition = value == '('
        otherConditions = type == TokenType.IDENTIFIER

        if integerConstant or stringConstant or keywordConstant or \
            unaryOpCondition or expressionCondition or otherConditions:

            self.compileExpression(node)                # expression
            while self._tokenizerValue() == ',':
                self._addSymbol(node, True)         # ,
                self.compileExpression(node)            # expression

        return node

    # DONE
    def compileStringConstant(self, parent):
        print("COMPILE STRING CONSTANT")
        if self.write_comments:
            parent.append(Comment('COMPILE STRING CONSTANT'))
        node = SubElement(parent, 'stringConstant')
        node.text = " " + str(self.tokenizer.stringVal()) + " "

        self.tokenizer.advance()

        return node

    # DONE
    def compileIntegerConstant(self, parent):
        print("COMPILE INTEGER CONSTANT")
        if self.write_comments:
            parent.append(Comment('COMPILE INTEGER CONSTANT'))
        node = SubElement(parent, 'integerConstant')
        node.text = " " + str(self.tokenizer.intVal()) + " "

        self.tokenizer.advance()

        return node


    ###########
    # HELPERS #
    ###########

    def _prettify(self, elem):
        """
        Return a pretty-printed XML string for the Element.
        """
        rough_string = ElementTree.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")

    def _tokenizerValue(self, raw = True):
        type = self.tokenizer.tokenType()
        if type == TokenType.KEYWORD:
            value = self.tokenizer.keyWord() if raw else self.tokenizer.keyWord().stringValue()
        elif type == TokenType.SYMBOL:
            value = self.tokenizer.symbol() if raw else saxutils.escape(self.tokenizer.symbol())
        elif type == TokenType.IDENTIFIER:
            value = self.tokenizer.identifier()
        elif type == TokenType.INT_CONST:
            value = self.tokenizer.intVal()
        elif type == TokenType.STRING_CONST:
            value = self.tokenizer.stringVal()
        else:
            value = None

        return value

    def _addKeyword(self, parent: Element, advance = False):
        keyword = self.tokenizer.keyWord()
        type = self.tokenizer.tokenType()

        if advance and self.tokenizer.hasMoreTokens():
            self.tokenizer.advance()

        child = SubElement(parent, type.tag())
        child.text = " " + keyword.stringValue() + " "

        return child

    def _addIdentifier(self, parent: Element, advance = False):
        identifier = self.tokenizer.identifier()
        type = self.tokenizer.tokenType()

        if advance and self.tokenizer.hasMoreTokens():
            self.tokenizer.advance()

        child = SubElement(parent, type.tag())
        child.text = " " + identifier + " "

        return child

    def _addSymbol(self, parent: Element, advance = False):
        symbol = self.tokenizer.symbol()
        type = self.tokenizer.tokenType()

        if advance and self.tokenizer.hasMoreTokens():
            self.tokenizer.advance()

        child = SubElement(parent, type.tag())
        child.text = " " + symbol + " "

        return child

    def _addSubroutineCall(self, node):
        self._addIdentifier(node, True)
        if self._tokenizerValue() == '(':                   # subroutineName
            self._addSymbol(node, True)                     # (
            self.compileExpressionList(node)                # expressionList
            self._addSymbol(node, True)                     # )

        else:                                               # className | varName
            self._addSymbol(node, True)                     # .
            self._addIdentifier(node, True)                 # subroutineName
            self._addSymbol(node, True)                     # (
            self.compileExpressionList(node)                # expressionList
            self._addSymbol(node, True)                     # )


if __name__ == "__main__":
    print("Inside CompilationEngine")
