from python.opcodes import *


COLUMN_WIDTH = 20


def print_header():
    co_code_index = "co_code Index"
    opcode = "Opcode"
    index = "Index"
    item = "Item"
    print(co_code_index + " " * (COLUMN_WIDTH - len(co_code_index)), end="")
    print(opcode + " " * (COLUMN_WIDTH - len(opcode)), end="")
    print(index + " " * (COLUMN_WIDTH - len(index)), end="")
    print(item + " " * (COLUMN_WIDTH - len(item)), end="")
    print()
    print("-" * len(co_code_index) + " " * (COLUMN_WIDTH - len(co_code_index)), end="")
    print("-" * len(opcode) + " " * (COLUMN_WIDTH - len(opcode)), end="")
    print("-" * len(index) + " " * (COLUMN_WIDTH - len(index)), end="")
    print("-" * len(item) + " " * (COLUMN_WIDTH - len(item)), end="")
    print()


def print_byte_code(co_code_index, opcode, index, item):
    co_code_index = str(co_code_index)
    if index is None:
        index = ""
    else:
        index = str(index)
    if item is None:
        item = ""
    else:
        item = f"({str(item)})"
    print(co_code_index + " " * (COLUMN_WIDTH - len(co_code_index)), end="")
    print(opcode + " " * (COLUMN_WIDTH - len(opcode)), end="")
    print(index + " " * (COLUMN_WIDTH - len(index)), end="")
    print(item + " " * (COLUMN_WIDTH - len(item)), end="")
    print()


class Disassembler:
    def __init__(self, byte_code):
        self.co_code, self.co_names, self.co_consts = byte_code
        self.pc = 0

    def dump(self):
        print_header()
        while self.pc < len(self.co_code):
            opcode = self.co_code[self.pc]
            self.visit(opcode)
            self.pc += 1

    def visit(self, opcode):
        opcode_name = opcode_to_name[opcode]
        opcode_visit = f"visit_{opcode_name}"
        getattr(self, opcode_visit)()

    def visit_UNARY_NEGATIVE(self):
        print_byte_code(self.pc, "UNARY_NEGATIVE", None, None)

    def visit_BINARY_MULTIPLY(self):
        print_byte_code(self.pc, "BINARY_MULTIPLY", None, None)

    def visit_BINARY_ADD(self):
        print_byte_code(self.pc, "BINARY_ADD", None, None)

    def visit_PRINT_ITEM(self):
        print_byte_code(self.pc, "PRINT_ITEM", None, None)

    def visit_PRINT_NEWLINE(self):
        print_byte_code(self.pc, "PRINT_NEWLINE", None, None)

    def visit_STORE_NAME(self):
        byte_code_pc = self.pc
        self.pc += 1
        index = self.co_code[self.pc]
        item = self.co_names[index]
        print_byte_code(byte_code_pc, "STORE_NAME", index, item)

    def visit_LOAD_CONST(self):
        byte_code_pc = self.pc
        self.pc += 1
        index = self.co_code[self.pc]
        item = self.co_consts[index]
        print_byte_code(byte_code_pc, "LOAD_CONST", index, item)

    def visit_LOAD_NAME(self):
        byte_code_pc = self.pc
        self.pc += 1
        index = self.co_code[self.pc]
        item = self.co_names[index]
        print_byte_code(byte_code_pc, "LOAD_CONST", index, item)
