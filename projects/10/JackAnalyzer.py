#!/usr/bin/env python3
import sys
import os
from pathlib import Path
from dataclasses import dataclass
from pprint import pprint

# TODO: FIX HANDLING OF OUTPUT PATH WHEN COMMAND LINE ARG HAS OUTPUT PATH (WITH EXT)

@dataclass
class FileData:
    """Class for keeping track of I/O info for each file."""
    filename: str
    input_dir: str
    input_ext: str
    output_dir: str
    output_ext: str

    def input_path(self) -> str:
        input_path = os.path.join(self.input_dir, self.filename)
        return os.path.splitext(input_path)[0] + self.input_ext

    def output_path(self) -> str:
        output_path = os.path.join(self.output_dir, self.filename)
        return os.path.splitext(output_path)[0] + "_out" + self.output_ext


class JackAnalyser:
    file_data = []
    input_ext: str = str(".jack")
    output_ext: str = str(".xml")

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

    def analyse(self):
        # TODO
        for file_data in self.file_data:
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
