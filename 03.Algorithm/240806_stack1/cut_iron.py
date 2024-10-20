T = int(input())
for tc in range(T):
    iron = input()
    new_iron = iron.replace('()', 'x')
    # print(new_iron)

    cutted = 0
    stack = []
    for elem in new_iron:
        if elem == '(':
            stack.append(elem)
        if elem == ')':
            stack.pop()
            cutted += 1
        if elem == 'x':
            cutted += len(stack)
            # print(cutted)

    print(f'#{tc+1} {cutted}')