from python.token import *


class Lexer:
    def __init__(self, src):
        self.src = src
        self.tokens = []

        self.pos = -1
        self.line = 0
        self.col = -1

        self.cur_char = None

    def lex(self):
        self.eat()
        while self.cur_char is not None:
            if self.cur_char in " \t":
                self.eat_spaces()
            elif self.cur_char.isalpha() or self.cur_char == "_":
                self.eat_identifier()
            elif self.cur_char.isdigit():
                self.eat_int()
            elif self.cur_char == "\n":
                newline = Token(self.line, self.col, NEWLINE, self.cur_char)
                self.tokens.append(newline)
                self.line += 1
                self.col = -1
                self.eat()
            elif self.cur_char == "(":
                lparen = Token(self.line, self.col, LPAREN, self.cur_char)
                self.tokens.append(lparen)
                self.eat()
            elif self.cur_char == ")":
                rparen = Token(self.line, self.col, RPAREN, self.cur_char)
                self.tokens.append(rparen)
                self.eat()
            elif self.cur_char == "=":
                eq = Token(self.line, self.col, EQ, self.cur_char)
                self.tokens.append(eq)
                self.eat()
            elif self.cur_char == "*":
                times = Token(self.line, self.col, TIMES, self.cur_char)
                self.tokens.append(times)
                self.eat()
            elif self.cur_char == "+":
                plus = Token(self.line, self.col, PLUS, self.cur_char)
                self.tokens.append(plus)
                self.eat()
            elif self.cur_char == "-":
                minus = Token(self.line, self.col, MINUS, self.cur_char)
                self.tokens.append(minus)
                self.eat()
            else:
                error = Token(self.line, self.col, ERROR, self.cur_char)
                self.tokens.append(error)
                self.eat()
        eof = Token(self.line, self.col, EOF, "")
        self.tokens.append(eof)
        return self.tokens

    def eat_spaces(self):
        # TODO: handle python ident
        self.eat()

    def eat_identifier(self):
        ident = self.cur_char
        start_col = self.col
        self.eat()
        while self.cur_char is not None and (
            self.cur_char.isalpha() or self.cur_char == "_"
        ):
            ident += self.cur_char
            self.eat()
        if ident in keywords:
            keyword = Token(self.line, start_col, keywords[ident], ident)
            self.tokens.append(keyword)
        else:
            name = Token(self.line, start_col, NAME, ident)
            self.tokens.append(name)

    def eat_int(self):
        integer = self.cur_char
        start_col = self.col
        self.eat()
        while self.cur_char is not None and self.cur_char.isdigit():
            integer += self.cur_char
            self.eat()
        int_tkn = Token(self.line, start_col, INT, integer)
        self.tokens.append(int_tkn)

    def eat(self):
        self.pos += 1
        self.col += 1
        if self.pos < len(self.src):
            self.cur_char = self.src[self.pos]
        else:
            self.cur_char = None
