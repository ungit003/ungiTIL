T = int(input())
for tc in range(T):
    N = int(input())
    case_list = []
    for _ in range(N):
        case = list(map(int, input().split()))
        case_list.append(case)

    mat = [[0] * 10 for _ in range(10)]
    for n in range(N):
        for i in range(case_list[n][0], case_list[n][2]+1):
            for j in range(case_list[n][1], case_list[n][3]+1):
                mat[i][j] += case_list[n][4]

    ans = 0
    for raw in mat:
        ans += raw.count(3)

    print(f'#{tc+1} {ans}')
