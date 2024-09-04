T = int(input())
for tc in range(T):
    N = int(input())

    find = False
    i = 1
    while True:
        if i * i * i == N:
            find = True
            break
        if i * i * i > N:
            break
        i += 1

    if find:
        ans = i
    else:
        ans = -1
    print(f'#{tc+1}', ans)