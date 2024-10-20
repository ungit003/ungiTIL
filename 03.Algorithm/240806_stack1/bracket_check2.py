T = int(input())
b_dict = {')': '(', '}': '{', ']': '['}
for tc in range(T):
    c = 1
    stack = []
    words = input()
    for elem in words:
        # print(elem)
        if elem in list(b_dict.values()):
            stack.append(elem)
            # print(stack)
        if elem in list(b_dict.keys()):
            if len(stack) == 0:
                c = 0
                break
            elif stack[-1] != b_dict[elem]:
                c = 0
                break
            else:
                stack.pop()
                # print(stack)
    if len(stack) != 0:
        c = 0
    print(f'#{tc+1} {c}')
