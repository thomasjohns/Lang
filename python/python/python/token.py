NAME = "NAME"
INT = "INT"

PRINT = "PRINT"

LPAREN = "LPAREN"
RPAREN = "RPAREN"

EQ = "EQ"

PLUS = "PLUS"
MINUS = "MINUS"
TIMES = "TIMES"

NEWLINE = "NEWLINE"
ERROR = "ERROR"
EOF = "EOF"


keywords = {
    "print": PRINT,
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
