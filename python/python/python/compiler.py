class Compiler:
    def __init__(self, ast):
        self.ast = ast
        self.byte_code = []

    def compile(self):
        self.visit(self.ast)
        return self.byte_code

    def visit(self, node):
        node_type = node.__class__.__name__
        node_visit = f"visit_{node_type}"
        getattr(self, node_visit)(node)

    def visit_Program(self, node):
        pass

    def visit_Assign(self, node):
        pass

    def visit_Print(self, node):
        pass

    def visit_UnaryOp(self, node):
        pass

    def visit_BinOp(self, node):
        pass

    def visit_Integer(self, node):
        pass

    def visit_Name(self, node):
        pass
