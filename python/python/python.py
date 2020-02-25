import sys

from python.lexer import Lexer
from python.parser import Parser
from python.ast_printer import ASTPrinter
from python.typer import Typer
from python.compiler import Compiler
from python.disassembler import Disassembler
from python.interpreter import Interpreter


with open(sys.argv[1], "r") as fp:
    src = fp.read()


lexer = Lexer(src)
tokens = lexer.lex()

print("------------------------ Tokens ------------------------")
for token in tokens:
    print(token)

parser = Parser(tokens)
ast = parser.parse()

print("------------------------ AST ---------------------------")
ast_printer = ASTPrinter(ast)
ast_printer.print()

print("------------------------ Type Checking -----------------")
typer = Typer(ast)
typer.check()

compiler = Compiler(ast)
byte_code = compiler.compile()

print("------------------------ Byte Code ---------------------")
dis = Disassembler(byte_code)
dis.dump()

print("------------------------ Output ------------------------")
interpreter = Interpreter(byte_code)
interpreter.interpret()
