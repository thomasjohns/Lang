NAME = "NAME"

INDENT = "INDENT"
DEDENT = "DEDENT"

IF = "IF"
ELSE = "ELSE"
WHILE = "WHILE"
PASS = "PASS"
PRINT = "PRINT"
TRUE = "TRUE"
FALSE = "FALSE"
NONE = "NONE"
DEF = "DEF"
CLASS = "CLASS"
NOT = "NOT"
AND = "AND"
OR = "OR"

INT = "INT"
FLOAT = "FLOAT"
STRING = "STRING"

COLON = "COLON"
COMMA = "COMMA"

LPAREN = "LPAREN"
RPAREN = "RPAREN"

EQ = "EQ"
EEQ = "EEQ"
NEQ = "NEQ"
LT = "LT"
LEQ = "LEQ"
GT = "GT"
GEQ = "GEQ"

PLUS = "PLUS"
MINUS = "MINUS"
TIMES = "TIMES"
DIV = "DIV"

NEWLINE = "NEWLINE"
ERROR = "ERROR"
EOF = "EOF"


keywords = {
    "pass": PASS,
    "print": PRINT,
    "if": IF,
    "else": ELSE,
    "while": WHILE,
    "True": TRUE,
    "False": FALSE,
    "None": NONE,
    "def": DEF,
    "class": CLASS,
    "not": NOT,
}


class Token:
    def __init__(self, line, col, category, lexeme):
        self.line = line
        self.col = col
        self.category = category
        self.lexeme = lexeme

    def __repr__(self):
        return (
            "Token("
            f"line={self.line}, col={self.col}, "
            f"category={self.category}, lexeme={repr(self.lexeme)}"
            ")"
        )
