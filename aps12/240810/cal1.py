T = 10
for tc in range(T):
    num = int(input())
    formula = input()

    stack = []
    operator = []
    for i in range(len(formula)):
        if formula[i].isdecimal():
            stack.append(int(formula[i]))
        else:
            operator.append(formula[i])

    while len(stack) != 1:
        a = stack.pop()
        b = stack.pop()
        c = operator.pop()
        d = a + b
        stack.append(d)

    print(f'#{tc+1}', *stack)