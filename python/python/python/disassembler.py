from python.opcodes import *


class Disassembler:
    def __init__(self, byte_code):
        self.co_code, self.co_names, self.co_consts = byte_code

    def dump(self):
        pass
