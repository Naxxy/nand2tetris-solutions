#!/usr/bin/env python3
import sys
import os
from pathlib import Path
from JackTokenizer import JackTokenizer, TokenType, Keyword
from CompilationEngine import CompilationEngine
from pprint import pprint
from FileData import FileData

# TODO: FIX HANDLING OF OUTPUT PATH WHEN COMMAND LINE ARG HAS OUTPUT PATH (WITH EXT)

class JackAnalyser:
    file_data = []
    input_ext: str = str(".jack")
    output_ext: str = str(".xml")

    # DONE
    def __init__(self, input_path: str, output_path: str):
        # Set input directory
        input_dir = input_path if os.path.isdir(input_path) else os.path.split(input_path)[0]

        # Set output directory
        if output_path == None:
            output_dir = input_path if os.path.isdir(input_path) else os.path.split(input_path)[0]
        else:
            output_dir = output_path


        # Set filedata for a directory
        self.file_data = []
        if os.path.isdir(input_path):
            filenames = (
                os.path.splitext(filename)[0]
                for filename in os.listdir(input_path)
                if filename.endswith(self.input_ext)
            )
            self.file_data = [FileData(filename, input_dir, self.input_ext, output_dir, self.output_ext) for filename in filenames]
        else:
            filename = os.path.splitext(os.path.split(input_path)[-1])[0]
            self.file_data = [FileData(filename, input_dir, self.input_ext, output_dir, self.output_ext)]

    # TODO
    def analyse(self):
        for file_data in self.file_data:
            print(file_data.input_path())
            compiler = CompilationEngine(file_data)
            # self._processTokensInFile(file_data)


    def _processTokensInFile(self, file_data: str):
        tokenizer = JackTokenizer(file_data.input_path())
        with open(file_data.token_output_path(), 'w') as fp:
            fp.write("<tokens>\n")
            while(tokenizer.hasMoreTokens()):

                type = tokenizer.tokenType()
                value = None
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
                    print("UNIMPLEMENTED: {}".format(type))
                    break

                # Write token to file
                print('{:40} - {:10}, {}'.format(type.tagWithValue(value), str(tokenizer.tokens), tokenizer.token_index))
                fp.write("\t" + type.tagWithValue(value) + "\n")
                tokenizer.advance()

            # End of tokenizing
            fp.write("</tokens>")


        print("> File data: \'{0}\', \'{1}\', \'{2}\'".format(
            file_data.filename, file_data.input_path(), file_data.output_path()))

def main():
    """
    Get the filename argument from command line args.
    Read the file contents and clean up lines by removing non-code strings.
    """
    # Make sure we have a filepath argument
    if len(sys.argv) < 2:
        sys.exit("Expected filepath argument for input.")

    input_path = Path(sys.argv[1])
    output_path = None

    if len(sys.argv) == 3:
        output_path = Path(sys.argv[2])

    if(not input_path.exists()):
        sys.exit("Filepath does not exist.")

    # Assemble code
    analyser = JackAnalyser(input_path.as_posix(), output_path.as_posix() if output_path else None)
    analyser.analyse()

if __name__ == "__main__":
    main()
