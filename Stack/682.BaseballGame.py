def BaseballGame(ops):
    stack = []

    for op in ops:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "D":
            stack.append(stack[-1] + stack[-1])
        elif op == "C":
            stack.pop()
        else:
            stack.append(int(op))
    return sum(stack)

if __name__ == '__main__':
    print(BaseballGame(["5","2","C","D","+"]))
            


