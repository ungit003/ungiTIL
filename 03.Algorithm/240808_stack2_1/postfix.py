T = int(input())
for tc in range(T):
    math_ex = input() + ' '

    ans = []
    stack = []

    for i in range(len(math_ex)):
        if math_ex[i] == ' ':
            break
        elif math_ex[i].isdecimal():
            ans.append(math_ex[i])
        else:
            if math_ex[i] == '/':
                while stack and stack[-1] == '*':
                    ans.append(stack.pop())
                stack.append(math_ex[i])
            if math_ex[i] == '+' or math_ex[i] == '-':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    ans.append(stack.pop())
                stack.append(math_ex[i])
            if math_ex[i] == '*':
                stack.append(math_ex[i])
    while stack:
        ans.append(stack.pop())

    print(f'#{tc+1}', ''.join(ans))

    # for elem in math_ex:
    #     if elem == ' ':
    #         break
    #     if not elem.isdecimal():
    #         stack.append(elem)
    #     if elem.isdecimal():
    #         ans.append(elem)
    #
    # while stack:
    #     ans.append(stack.pop())



