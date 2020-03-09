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


class BoolOp(ASTNode):
    """`a or b or c` has `op='or'` and `values=[a, b, c]`"""
    def __init__(self, op, values):
        self.op = op
        self.values = values


class Compare(ASTNode):
    def __init__(self, left, op, comparators):
        self.left = left
        self.op = op
        self.comparators = comparators


class And(ASTNode):
    pass


class Or(ASTNode):
    pass


class Constant(ASTNode):
    def __init__(self, value):
        self.value = value


class Str(ASTNode):
    def __init__(self, s):
        self.s = s


class NameCtx:
    LOAD = "LOAD"
    STORE = "STORE"


class Name(ASTNode):
    def __init__(self, value, ctx):
        self.value = value
        self.ctx = ctx
