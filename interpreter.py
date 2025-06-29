# lexer.py
import re

TOKEN_SPEC = [
    ('NUMBER',   r'\d+'),
    ('ID',       r'[a-zA-Z_]\w*'),
    ('ASSIGN',   r'='),
    ('PRINT',    r'print'),
    ('PLUS',     r'\+'),
    ('SKIP',     r'[ \t]+'),
    ('NEWLINE',  r'\n'),
]

def tokenize(code):
    tokens = []
    tok_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in TOKEN_SPEC)
    for match in re.finditer(tok_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'SKIP':
            continue
        tokens.append((kind, value))
    return tokens

