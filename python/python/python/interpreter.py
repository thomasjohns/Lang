from python.opcodes import *


class Stack:
    def __init__(self):
        self._data = []

    def push(self, x):
        self._data.append(x)

    def pop(self):
        return self._data.pop()


class Interpreter:
    def __init__(self, byte_code):
        self.co_code, self.co_names, self.co_consts = byte_code
        self.co_values = [None] * len(self.co_names)
        self.stack = Stack()
        self.pc = 0

    def interpret(self):
        while self.pc < len(self.co_code):
            opcode = self.co_code[self.pc]
            self.visit(opcode)
            self.pc += 1

    def visit(self, opcode):
        opcode_name = opcode_to_name[opcode]
        opcode_visit = f"visit_{opcode_name}"
        getattr(self, opcode_visit)()

    def visit_UNARY_NEGATIVE(self):
        top = self.stack.pop()
        self.stack.push(-top)

    def visit_BINARY_MULTIPLY(self):
        left = self.stack.pop()
        right = self.stack.pop()
        self.stack.push(left * right)

    def visit_BINARY_ADD(self):
        left = self.stack.pop()
        right = self.stack.pop()
        self.stack.push(left + right)

    def visit_PRINT_ITEM(self):
        top = self.stack.pop()
        print(top, end="")

    def visit_PRINT_NEWLINE(self):
        print()

    def visit_STORE_NAME(self):
        self.pc += 1
        index = self.co_code[self.pc]
        top = self.stack.pop()
        self.co_values[index] = top

    def visit_LOAD_CONST(self):
        self.pc += 1
        index = self.co_code[self.pc]
        value = self.co_consts[index]
        self.stack.push(value)

    def visit_LOAD_NAME(self):
        self.pc += 1
        index = self.co_code[self.pc]
        value = self.co_values[index]
        self.stack.push(value)
