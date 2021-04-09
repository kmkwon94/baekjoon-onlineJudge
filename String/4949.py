while True:
    string = input()
    stack = []
    true_flag = 1
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':  #스택이 비워져 있지 않고 마지막이 '(' 이면
                stack.pop()
            else:
                true_flag = 0
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                true_flag = 0
                break
    if string == '.':
        break
    print("yes" if true_flag and not(stack) else "no")
print("yes")