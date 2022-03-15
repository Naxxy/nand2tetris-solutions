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

    def __init__(self, file_data: FileData):
        self.tokenizer = JackTokenizer(file_data.input_path())
        self.fp_in = open(file_data.input_path(), 'r')
        self.file_data = file_data
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
        error = None

        print("COMPILE CLASS")
        root.append(Comment('COMPILE CLASS'))

        child = self._addKeyword(root, True)          # Class
        child = self._addIdentifier(root, True)       # ClassName
        child = self._addSymbol(root, True)           # {

        try:
            type = TokenType.KEYWORD
            while type == TokenType.KEYWORD:
                type = self.tokenizer.tokenType()
                value = self.tokenizer.keyWord()
                if value in [Keyword.CONSTRUCTOR, Keyword.FUNCTION, Keyword.METHOD]:
                    self.compileSubroutine(root)
                elif value in [Keyword.STATIC, Keyword.FIELD]:
                    self.compileClassVarDec(root)

            child = self._addSymbol(root, True)           # }
        except Exception as e:
            error = e
        finally:
            with open(self.file_data.output_path(), 'w') as fp:
                fp.write(self._prettify(root))
            if error:
                raise error

    # DONE
    def compileClassVarDec(self, parent):
        print("COMPILE CLASS VARIABLE DECLARATION")
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

    def compileStatements(self, parent):
        pass

    def compileLet(self):
        pass

    def compileIf(self):
        pass

    def compileWhile(self):
        pass

    def compileDo(self):
        pass

    def compileReturn(self):
        pass

    def compileExpression(self):
        pass

    def compileTerm(self):
        pass

    def compileExpressionList(self):
        pass

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

        if advance:
            self.tokenizer.advance()

        child = SubElement(parent, type.tag())
        child.text = " " + keyword.stringValue() + " "

        return child

    def _addIdentifier(self, parent: Element, advance = False):
        identifier = self.tokenizer.identifier()
        type = self.tokenizer.tokenType()

        if advance:
            self.tokenizer.advance()

        child = SubElement(parent, type.tag())
        child.text = " " + identifier + " "

        return child

    def _addSymbol(self, parent: Element, advance = False):
        symbol = self.tokenizer.symbol()
        type = self.tokenizer.tokenType()

        if advance:
            self.tokenizer.advance()

        child = SubElement(parent, type.tag())
        child.text = " " + saxutils.escape(symbol) + " "

        return child


if __name__ == "__main__":
    print("Inside CompilationEngine")
