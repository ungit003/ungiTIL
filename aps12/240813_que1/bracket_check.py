T = int(input())
for tc in range(T):
    words = input()

    result = 1
    stack = []
    for i in words:
        if i == '(' or i == '{':
            stack.append(i)
        if i == ')':
            if len(stack) == 0:
                result = 0
                break
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    result = 0
                    break
        if i == '}':
            if len(stack) == 0:
                result = 0
                break
            else:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    result = 0
                    break
    if len(stack) != 0:
        result = 0

    print(f'#{tc+1} {result}')