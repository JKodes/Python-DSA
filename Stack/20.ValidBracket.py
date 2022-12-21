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
    














if __name__ == '__main__':
    def(brackets ={ } )