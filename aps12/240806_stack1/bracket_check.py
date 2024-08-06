T = int(input())
for tc in range(T):
    check = input()
    stack = []
    c = 1

    for elem in check:
        # print(elem)
        if elem == '(':
            stack.append(elem)
            # print(stack)
        elif elem == ')':
            # print(len(stack))
            # print(stack)
            if len(stack) == 0:
                c = -1
                break
            elif '(' not in stack:
                c = -1
                break
            else:
                stack.pop()
                # print(stack)
    if len(stack) != 0:
        c = -1
    print(f'#{tc + 1} {c}')