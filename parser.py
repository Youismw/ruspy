# parser.py
def parse(tokens):
    it = iter(tokens)
    ast = []
    try:
        while True:
            kind, val = next(it)
            if kind == 'ID':
                next_kind, next_val = next(it)
                if next_kind == 'ASSIGN':
                    rhs_kind, rhs_val = next(it)
                    ast.append(('assign', val, rhs_val))
            elif kind == 'PRINT':
                expr_kind, expr_val = next(it)
                ast.append(('print', expr_val))
    except StopIteration:
        pass
    return ast

