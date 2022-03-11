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

    # DONE
    def compileClass(self):
        """
        <class>
          <keyword> class </keyword>
          <identifier> Main </identifier>
          <symbol> { </symbol>
          <subroutineDec> ... </subroutineDec>
          <symbol> } </symbol>
        </class>
        """
        root = Element("class")

        child = self._addKeyword(root)          # Class
        child = self._addIdentifier(root)       # ClassName
        child = self._addSymbol(root)           # {

        # self.compileSubroutine()                # subroutineDec


        # child = self._addSymbol(root)           # }

        with open(self.file_data.output_path(), 'w') as fp:
            fp.write(self._prettify(root))


    def compileClassVarDec(self):
        """
        <classVarDec>
          <keyword> static </keyword>
          <keyword> boolean </keyword>
          <identifier> test </identifier>
          <symbol> ; </symbol>
        </classVarDec>
        """
        pass

    def compileSubroutine(self):
        pass

    def compileParameterList(self):
        pass

    def compileSubroutineBody(self):
        pass

    def compileVarDec(self):
        """
        Example:
            <varDec>
              <keyword> var </keyword>
              <identifier> Array </identifier>
              <identifier> a </identifier>
              <symbol> ; </symbol>
            </varDec>
        """

        # Starts with 'var'
        # followed by type = identifier?
        # followed by var name = identifier?
        # loop - if starts with comma symbol, repeat
        # Terminated by terminal symbol
        pass

    def compileStatements(self):
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
