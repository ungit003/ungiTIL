T = 10
for tc in range(T):
    num = int(input())
    formula = input()

    stack = []
    operator = []
    res = []
    for i in range(len(formula)):
        if formula[len(formula)-1-i].isdecimal():
            stack.append((formula[len(formula)-1-i]))
        else:
            operator.append(formula[len(formula)-1-i])
    print(stack, operator)

    res.append(stack.pop())
    while operator:
        a = operator.pop()
        b = stack.pop()

        if a == '+':
            res.append(b)
            res.append(a)
        if a == '*':
            if res[-1].isdecimal():
                res.append(b)
                res.append(a)
            else:
                c = res.pop()
                res.append(b)
                res.append(a)
                res.append(c)
    print(res)

    stack2 = []
    for elem in res:
        if elem.isdecimal():
            stack2.append(elem)
        else:
            a1 = int(stack2.pop())
            a2 = int(stack2.pop())
            if elem == '+':
                a2 += a1
                stack2.append(a2)
            if elem == '*':
                a2 *= a1
                stack2.append(a2)

    print(f'#{tc+1}', *stack2)
