T = int(input())

def switch(mat):
    for i in range(N+2):
        for j in range(N+2):
            if i < j:
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

def counting(pad):
    counts = 0
    for raw in pad:
        # str_raw = []
        # for i in range(len(raw)):
        #     str_raw.append(str(raw[i]))
        # raw_j = ''.join(str_raw)
        # print(raw_j)
        # ans = '0' + '1' * K + '0'
        # a = raw_j.count(ans)
        ans_list = [0] + [1] * K + [0]
        for i in range(N - K + 1):      # 15 3 / 17 5 '13'
            if raw[i: i + K + 2] == ans_list:
                counts += 1
    return counts

for tc in range(T):
    N, K = map(int, input().split())
    pad = [[0]*(N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+2)]
    # print(pad)

    a = counting(pad)

    switch(pad)
    b = counting(pad)

    print(f'#{tc+1} {a+b}')