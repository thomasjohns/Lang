class LineWriter:
    def __init__(self, indent_size):
        self.indent_size = indent_size
        self.carriage_return = True
        self.spaces = 0

    def indent(self):
        self.spaces += self.indent_size

    def dedent(self):
        self.spaces -= self.indent_size

    def write(self, msg=""):
        if self.carriage_return:
            print(self.spaces * " " + msg, end="")
        else:
            print(msg, end="")
        self.carriage_return = False

    def writeln(self, msg=""):
        if self.carriage_return:
            print(self.spaces * " " + msg)
        else:
            print(msg)
        self.carriage_return = True


class ASTPrinter:
    def __init__(self, ast, indent=2):
        self.ast = ast
        self.writer = LineWriter(indent)

    def print(self):
        self.visit(self.ast)
        self.writer.writeln()

    def visit(self, node):
        node_type = node.__class__.__name__
        node_visit = f"visit_{node_type}"
        getattr(self, node_visit)(node)

    def visit_Program(self, node):
        self.writer.writeln(f"{node.__class__.__name__}(")
        self.writer.indent()
        self.writer.writeln("stmts=[")
        self.writer.indent()
        for stmt in node.stmts:
            self.visit(stmt)
            self.writer.writeln(",")
        self.writer.dedent()
        self.writer.write("]")
        self.writer.writeln(",")
        self.writer.dedent()
        self.writer.write(")")

    def visit_Assign(self, node):
        self.writer.writeln(f"{node.__class__.__name__}(")
        self.writer.indent()
        self.writer.write("name=")
        self.visit(node.name)
        self.writer.writeln(",")
        self.writer.write("expr=")
        self.visit(node.expr)
        self.writer.writeln(",")
        self.writer.dedent()
        self.writer.write(")")

    def visit_Print(self, node):
        self.writer.writeln(f"{node.__class__.__name__}(")
        self.writer.indent()
        self.writer.write("expr=")
        self.visit(node.expr)
        self.writer.writeln(",")
        self.writer.dedent()
        self.writer.write(")")

    def visit_UnaryOp(self, node):
        self.writer.writeln(f"{node.__class__.__name__}(")
        self.writer.indent()
        self.writer.writeln(f"op='{node.op.lexeme}',")
        self.writer.write(f"operand=")
        self.visit(node.operand)
        self.writer.writeln(",")
        self.writer.dedent()
        self.writer.write(")")

    def visit_BinOp(self, node):
        self.writer.writeln(f"{node.__class__.__name__}(")
        self.writer.indent()
        self.writer.write("left=")
        self.visit(node.left)
        self.writer.writeln(",")
        self.writer.writeln(f"op='{node.op.lexeme}',")
        self.writer.write("right=")
        self.visit(node.right)
        self.writer.writeln(",")
        self.writer.dedent()
        self.writer.write(")")

    def visit_Constant(self, node):
        self.writer.write(f"{node.__class__.__name__}(value={node.value})")

    def visit_Name(self, node):
        self.writer.write(
            f"{node.__class__.__name__}(value={node.value}, ctx={node.ctx})"
        )
