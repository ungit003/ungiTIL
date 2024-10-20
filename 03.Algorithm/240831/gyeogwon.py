def remove_and_score(s):
    global stack
    score = 0
    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
            score += 1
            if i != len(s) - 1 and s[i] == s[i+1]:
                stack.append(s[i])
            else:
                score += 1
        else:
            stack.append(s[i])
    return score


def combo_score(stack):
    score = 0
    for i in range(len(stack)):
        if i != len(stack) - 1 and ord(stack[i+1]) == ord(stack[i]) + 1:
            score += 1
            if i != len(stack) - 2 and ord(stack[i+2]) != ord(stack[i+1]) + 1:
                score += 1
        elif i == len(stack) - 1 and ord(stack[i]) == ord(stack[i-1]) + 1:
            score += 1
    return score


T = int(input())
for tc in range(1, T+1):
    string = list(input())
    stack = []
    result1 = remove_and_score(string)
    result2 = combo_score(stack)
    print(f'#{tc}', result1 + result2)