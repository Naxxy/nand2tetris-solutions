#!/usr/bin/env python

class CompilationEngine:
    fp = None

    def __init__(self, filepath: str):
        self.fp = open()

    def compileClass(self):
        pass

    def compileClassVarDec(self):
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




if __name__ == "__main__":
    print("Inside CompilationEngine")
