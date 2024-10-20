T = 10
N = 100
for _ in range(T):
    tc = int(input())
    mat = [[s for s in input()] for _ in range(N)]

    longest = 0
    for row in mat:
        # print(row)
        judge_row = ''.join(row)
        # print(judge_row)
        for i in range(N):
            for start in range(N-i+1):
                if judge_row[start:start+i+1] == judge_row[start:start+i+1][::-1]:
                    if longest < len(judge_row[start:start+i+1]):
                        longest = len(judge_row[start:start+i+1])

    for col in zip(*mat):
        cola = list(col)
        # print(col)
        judge_col = ''.join(cola)
        # print(cola)
        # print(judge_col)
        for i in range(N):
            for start in range(N-i+1):
                if judge_col[start:start+i+1] == judge_col[start:start+i+1][::-1]:
                    if longest < len(judge_col[start:start+i+1]):
                        longest = len(judge_col[start:start+i+1])

    print(f'#{tc}', longest)