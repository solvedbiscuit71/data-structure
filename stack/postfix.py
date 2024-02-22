import operator

def util(s: str) -> list[int | str]:
    tokens = s.split(' ')
    expr = [ int(token) if token.isdigit() else token for token in tokens ]
    return expr


def infix_to_postfix(expr: list[int | str]):
    op_stack = []
    op_prec = {
        '(': -1,
        '+': 0,
        '-': 0,
        '*': 1,
        '/': 1,
    }
    is_open = lambda c: c == '('
    is_close = lambda c: c == ')'
    postfix = []

    for token in expr:
        if type(token) is int:
            postfix.append(token)
        elif type(token) is str:
            if is_open(token):
                op_stack.append(token)
            elif is_close(token):
                while op_stack:
                    op = op_stack.pop()
                    if is_open(op):
                        break
                    postfix.append(op)
            else:
                try:
                    while op_stack and op_prec[op_stack[-1]] >= op_prec[token]: # type: ignore
                        postfix.append(op_stack.pop())
                    op_stack.append(token)
                except KeyError:
                    raise ValueError
        else:
            raise TypeError
    while op_stack:
        postfix.append(op_stack.pop())
    return postfix


def evaluate_postfix(expr: list[int | str]) -> int:
    res_stack = []
    op_mapper = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    for token in expr:
        if type(token) is int:
            res_stack.append(token)
        elif type(token) is str:
            try:
                b, a = res_stack.pop(), res_stack.pop()
                res_stack.append(op_mapper[token](a, b))
            except KeyError:
                raise ValueError
        else:
            raise TypeError
    return res_stack.pop() # type: ignore

if __name__ == "__main__":
    expr = "5 + 8 * ( 3 + 6 ) / 5 * ( 3 + 3 )"
    postfix_expr = infix_to_postfix(util(expr))
    value = evaluate_postfix(postfix_expr)
    print("Infix:", expr)
    print("Postfix:", ' '.join(map(str, postfix_expr)))
    print("Evaluated value:", value)
