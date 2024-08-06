T = int(input())
for tc in range(T):
    check = 0
    word = input()
    if word == word[::-1]:
        check = 1
    print(f'#{tc+1} {check}')
