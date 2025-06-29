# interpreter.py
import lexer
import parser
import subprocess
import json

def load_code(filename):
    with open(filename) as f:
        return f.read()

def evaluate(ast):
    env = {}
    for node in ast:
        if node[0] == 'assign':
            _, var, val = node
            env[var] = int(val)
        elif node[0] == 'print':
            _, expr = node
            print(env.get(expr, expr))
    return env

def main():
    code = load_code("examples/hello.mini")
    tokens = lexer.tokenize(code)
    ast = parser.parse(tokens)

    # Pass to Java for semantic analysis
    with open("temp_ast.json", "w") as f:
        json.dump(ast, f)
    subprocess.run(["java", "-cp", "semantic", "SemanticAnalyzer", "temp_ast.json"])

    evaluate(ast)

if __name__ == "__main__":
    main()

