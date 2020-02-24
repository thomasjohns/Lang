class Stack:
    def __init__(self):
        self._data = []

    def push(self, x):
        self._data.append(x)

    def pop(self):
        self._data.pop()


class Interpreter:
    def __init__(self, byte_code):
        self.co_code, self.co_names, self.co_consts = byte_code
        self.co_values = [None] * len(self.co_code)
        self.stack = Stack()
        self.pc = 0

    def interpret(self):
        print("interpeting")
