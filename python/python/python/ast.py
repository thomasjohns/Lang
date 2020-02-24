class ASTNode:
    pass


class Program(ASTNode):
    def __init__(self, stmts):
        self.stmts = stmts


class Assign(ASTNode):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr


class Print(ASTNode):
    def __init__(self, expr):
        self.expr = expr


class UnaryOp(ASTNode):
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand


class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Integer(ASTNode):
    def __init__(self, value):
        self.value = value


class NameCtx:
    LOAD = "LOAD"
    STORE = "STORE"


class Name(ASTNode):
    def __init__(self, value, ctx):
        self.value = value
        self.ctx = ctx
