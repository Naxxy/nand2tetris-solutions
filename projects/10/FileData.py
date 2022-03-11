import os
from dataclasses import dataclass

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

    def token_output_path(self) -> str:
        output_path = os.path.join(self.output_dir, self.filename)
        return os.path.splitext(output_path)[0] + "T" + self.output_ext
