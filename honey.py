"""
1. 가로 m 벌통 * 2 고르기
    1. n * n 에서 무작위로 고르고 그게 조건에 부합하는가? 찾기
    2. 가로 m을 안에 놓을 수 있는지 찾기 v
    
2. 안에서 제곱합 최댓값 구하기
    - 부분집합 중에 합이 C보다 작거나 같은거
    - 제곱 합
"""
def finder():
    ans = 0
    for x1 in range(N - M + 1):
        for y1 in range(N):
            for x2 in range(N - M + 1):
                for y2 in range(N):
                    if y1 == y2 and abs(x1 - x2) < M:
                        continue
                    max1 = calculator(y1, x1)
                    max2 = calculator(y2, x2)
                    ans = max(ans, max1 + max2)
    return ans


def calculator(y1, x1):
    arr = []
    for x in range(x1, x1 + M):
        arr.append(mat[y1][x])
    
    max_sum = 0
    for i in range(1 << M):
        subset = []
        for j in range(M):
            if i & (1 << j):
                subset.append(arr[j])
        if sum(subset) > C:
            continue
        sums = sum([elem**2 for elem in subset])
        max_sum = max(sums, max_sum)
    return max_sum


T = int(input())
for tc in range(T):
    N, M, C = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    
    ans = finder()
    print(f'#{tc+1} {ans}')