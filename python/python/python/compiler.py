from python.ast import NameCtx
from python.token import *
from python.opcodes import *


class Compiler:
    def __init__(self, ast):
        self.ast = ast

        self.co_code = []
        self.co_names = []
        self.co_consts = []

    def compile(self):
        self.visit(self.ast)
        return self.co_code, self.co_names, self.co_consts

    def visit(self, node):
        node_type = node.__class__.__name__
        node_visit = f"visit_{node_type}"
        getattr(self, node_visit)(node)

    def visit_Program(self, node):
        for stmt in node.stmts:
            self.visit(stmt)

    def visit_Assign(self, node):
        self.visit(node.expr)
        self.visit(node.name)

    def visit_Print(self, node):
        self.visit(node.expr)
        self.co_code.append(PRINT_ITEM)
        self.co_code.append(PRINT_NEWLINE)

    def visit_UnaryOp(self, node):
        self.visit(node.operand)
        if node.op.category == MINUS:
            self.co_code.append(UNARY_NEGATIVE)

    def visit_BinOp(self, node):
        self.visit(node.left)
        self.visit(node.right)
        if node.op.category == PLUS:
            self.co_code.append(BINARY_ADD)
        elif node.op.category == MINUS:
            self.co_code.append(UNARY_NEGATIVE)
            self.co_code.append(BINARY_ADD)
        elif node.op.category == TIMES:
            self.co_code.append(BINARY_MULTIPLY)

    def visit_Integer(self, node):
        self.co_code.append(LOAD_CONST)
        index = len(self.co_consts)
        self.co_consts.append(node.value)
        self.co_code.append(index)

    def visit_Name(self, node):
        if node.ctx == NameCtx.LOAD:
            self.co_code.append(LOAD_NAME)
        elif node.ctx == NameCtx.STORE:
            self.co_code.append(STORE_NAME)

        if node.value in self.co_names:
            index = self.co_names.index(node.value)
        else:
            index = len(self.co_names)
            self.co_names.append(node.value)
        self.co_code.append(index)
