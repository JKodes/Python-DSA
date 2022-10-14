def EvaluateReversePolishNotation(tokens):
    stack = []

    for token in tokens:
        if token  == "+":
            stack.append(stack.pop() + stack.op())
        elif token == "-":
            x, y = stack.pop() , stack.pop()
            stack.append(y - x)
        elif token == "*":
            stack.append(stack.pop() * stack.op())
        elif token == "/":
            x, y = stack.pop() , stack.pop()
            stack.append(int(y / x))
    return stack[0]


