def valid_parenthesis(s: str) -> bool:
    memo = { ')': '(', ']': '[', '}': '{' }
    stk = []
    try:
        for c in s:
            if c in memo:
                if stk[-1] == memo[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
    except IndexError:
        return False
    return not stk


s1 = "((({}{}[]))"      # it's not valid
s2 = "()()({{}[]})"     # it's valid
s3 = ")()()({{}[]})"    # it's not valid

print(s1, valid_parenthesis(s1))
print(s2, valid_parenthesis(s2))
print(s3, valid_parenthesis(s3))

