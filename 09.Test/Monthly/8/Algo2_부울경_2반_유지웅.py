# 1. 입력값 받기.
T = int(input())
for tc in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

# 2. 문제 풀이에 필요한 리스트 만들기.
    line_list = []                                      # 3과 8 사이의 N에 따른 순열 리스트 만들기.
    if N == 3:
        for a in range(N):
            for b in range(N):
                for c in range(N):
                    elem = [a, b, c]
                    if len(set(elem)) == N:
                        line_list.append([a, b, c])

    if N == 4:
        for a in range(N):
            for b in range(N):
                for c in range(N):
                    for d in range(N):
                        elem = [a, b, c, d]
                        if len(set(elem)) == N:
                            line_list.append([a, b, c, d])

    if N == 5:
        for a in range(N):
            for b in range(N):
                for c in range(N):
                    for d in range(N):
                        for e in range(N):
                            elem = [a, b, c, d, e]
                            if len(set(elem)) == N:
                                line_list.append([a, b, c, d, e])


    if N == 6:
        for a in range(N):
            for b in range(N):
                for c in range(N):
                    for d in range(N):
                        for e in range(N):
                            for f in range(N):
                                elem = [a, b, c, d, e, f]
                                if len(set(elem)) == N:
                                    line_list.append([a, b, c, d, e, f])

    if N == 7:
        for a in range(N):
            for b in range(N):
                for c in range(N):
                    for d in range(N):
                        for e in range(N):
                            for f in range(N):
                                for g in range(N):
                                    elem = [a, b, c, d, e, f, g]
                                    if len(set(elem)) == N:
                                        line_list.append([a, b, c, d, e, f, g])

    if N == 8:
        for a in range(N):
            for b in range(N):
                for c in range(N):
                    for d in range(N):
                        for e in range(N):
                            for f in range(N):
                                for g in range(N):
                                    for h in range(N):
                                        elem = [a, b, c, d, e, f, g, h]
                                        if len(set(elem)) == N:
                                            line_list.append([a, b, c, d, e, f, g, h])

# 3. 줄 선 외계인에 대한 외계인 사이의 위험도 계산하기.
    min_danger = float('INF')                           # 최솟값을 예측하기 힘듦으로 무한대로 임시값 지정하기.
    for line in line_list:                              # 줄 세운 리스트에서 값을 불러오기.
        danger = 0                                      # 외계인 사이의 값들을 danger 에 더하기.
        for i in range(N - 1):
            danger += mat[line[i]][line[i + 1]]
            if danger >= min_danger:                    # 더하는 와중에 이미 최솟값을 넘었다면, 멈추기.
                break
        if min_danger > danger:                         # 더한 결과가 최솟값보다 작다면, 최솟값 변경하기.
            min_danger = danger

# 4. 결과 출력하기.
    print(f'#{tc + 1}', min_danger)