def ValidBracket(brackets):
    stack = []
    cto = {"]": "[", "}" : "}",  ")" : "("}

    for bracket in brackets:
        if bracket in cto:
            if stack and stack[-1] == cto[bracket]:
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)

    return True if not stack else False
    




if __name__ == '__main__':
    print(ValidBracket(brackets = "()[]" ))