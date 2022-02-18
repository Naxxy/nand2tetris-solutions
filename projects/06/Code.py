
test_code = [
	["D",      "A",     "JNE"],
	["D",      "D+A",   ""],
	["M",      "D",     "JEQ"],
	["AM",      "-1",     "JGT"],
    ["A",      "D&M",     "JLT"],
    ["",       "0",      "JMP"]
]

class Code:
    def __init__(self):
        print("create code class")

    # DONE
    def dest(self, value: str) -> str:
        out = [
            "A" in value,
            "D" in value,
            "M" in value
        ]
        out = [str(int(x)) for x in out]

        return "".join(out)

    # DONE
    def comp(self, value: str) -> str:
        switcher = {
        # a=0
        "0":      "0" + "101010",
        "1":      "0" + "111111",
        "-1":     "0" + "111010",
        "D":      "0" + "001100",
        "A":      "0" + "110000",
        "!D":     "0" + "001101",
        "!A":     "0" + "110001",
        "-D":     "0" + "001111",
        "-A":     "0" + "110011",
        "D+1":    "0" + "011111",
        "A+1":    "0" + "110111",
        "D-1":    "0" + "001110",
        "A-1":    "0" + "110010",
        "D+A":    "0" + "000010",
        "D-A":    "0" + "010011",
        "A-D":    "0" + "000111",
        "D&A":    "0" + "000000",
        "D|A":    "0" + "010101",

        # a=1
        "M":      "1" + "110000",
        "!M":     "1" + "110001",
        "-M":     "1" + "110011",
        "M+1":    "1" + "110111",
        "M-1":    "1" + "110010",
        "D+M":    "1" + "000010",
        "D-M":    "1" + "010011",
        "M-D":    "1" + "000111",
        "D&M":    "1" + "000000",
        "D|M":    "1" + "010101"
        }
        return switcher.get(value, "1" + "111111")

    # DONE
    def jump(self, value: str) -> str:
        switcher = {
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111"
        }

        return switcher.get(value, "000")


if __name__ == "__main__":
    code = Code()
    for line in test_code:
        d = code.dest(line[0])
        c = code.comp(line[1])
        j = code.jump(line[2])
        print("{:16}\t{:4}{:4}{:4}".format(
            " ".join([d, c, j]),
            line[0],
            line[1],
            line[2]
        ))
