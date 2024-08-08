T = int(input())
for tc in range(T):
    words = input().split()

    cnt = 0
    result = 0
    stack = []
    for i in range(len(words)):
        if words[i].isdecimal():
            cnt += 1
    if cnt * 2 != len(words):
        result = -1
    else:
        for elem in words:
            if elem.isdecimal():
                stack.append(int(elem))
            elif not elem.isdecimal():
                if elem == '.':
                        if len(stack) != 1:
                            result = -1
                        else:
                            result = 1
                    elif elem == '+':
                        cal = stack.pop()
                        cal += stack.pop()
                        stack.append(cal)
                    elif elem == '-':
                        cal = stack.pop()
                        cal -= stack.pop()
                        stack.append(cal)
                    elif elem == '*':
                        cal = stack.pop()
                        cal *= stack.pop()
                        stack.append(cal)
                    elif elem == '/':
                        cal = stack.pop()
                        cal /= stack.pop()
                        stack.append(int(cal))

    if result == -1:
        print(f'#{tc+1} error')
    if result == 1:
        print(f'#{tc+1} {stack[0]}')


    # cnt = 0
    # for i in range(len(words)):
    #     if words[i].isdecimal():
    #         cnt += 1
    # if cnt * 2 != len(words):
    #     print(f'#{tc+1} error')
    #     continue
    #
    # stack = []
    # for i in range(len(words)):
    #     if words[i] == '.':
    #         if len(stack) > 1:
    #             print(f'#{tc + 1} error')
    #         else:
    #             print(f'#{tc+1}', stack[0])
    #         break
    #     if words[i].isdecimal():
    #         stack.append(int(words[i]))
    #     if not words[i].isdecimal():
    #         if len(stack) < 2:
    #             print(stack)
    #             print(f'#{tc + 1} error')
    #     cal = stack.pop()
    #     if words[i] == '+':
    #         cal += stack.pop()
    #         stack.append(cal)
    #     elif words[i] == '-':
    #         cal -= stack.pop()
    #         stack.append(cal)
    #     elif words[i] == '*':
    #         cal *= stack.pop()
    #         stack.append(cal)
    #     elif words[i] == '/':
    #         cal /= stack.pop()
    #         stack.append(cal)




