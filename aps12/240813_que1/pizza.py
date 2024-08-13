T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))

    count = -1
    fire = []
    for i in range(N):
        count += 1
        fire.append([count, C.pop(0), 0])   # 피자번호, 치즈, 들어간 시간
    # print(fire)
    # print('*' * 100)

    count2 = 0
    rotating = 1
    while True:
        if count2 == N - 1:
            for i in range(N):
                if fire[i][0] != 'x':
                    a = fire[i][0]
            print(f'#{tc+1} {a + 1}')
            break
        # print(rotating)
        fire.append(fire.pop(0))
        # print(fire)
        for i in range(len(fire)):
            if (rotating - fire[i][2]) % N == 0:
                fire[i][1] = fire[i][1] // 2
            # print(fire)
        if fire[0][1] == 0:
            if len(C) != 0:
                fire.pop(0)
                count += 1
                fire.insert(0, [count, C.pop(0), rotating])
                # print(C)
                # print(fire)
            else:
                fire.pop(0)
                fire.insert(0, ['x', 999, rotating])
                count2 += 1
                # print(fire)

        rotating += 1



