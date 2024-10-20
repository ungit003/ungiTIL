# 1. 순열 수입해오기.
from itertools import permutations

# 2. 입력값 받기.
T = int(input())
for tc in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

# 3. 문제 풀이에 필요한 리스트 만들기.
    arr = list(range(N))                                       # 외계인을 0 ~ N-1 으로 인덱싱하기.
    nPn = list(permutations(arr, N))                           # 외계인을 줄 세운 리스트 만들기.

# 4. 줄 선 외계인에 대한 외계인 사이의 위험도 계산하기.
    min_danger = float('INF')                                  # 최솟값을 예측하기 힘듦으로 무한대로 임시값 지정하기.
    for line in nPn:                                           # 줄 세운 리스트에서 값을 불러오기.
        danger = 0                                             # 외계인 사이의 값들을 danger 에 더하기.
        for i in range(N-1):
            danger += mat[line[i]][line[i+1]]
            if danger >= min_danger:                           # 더하는 와중에 이미 최솟값을 넘었다면, 멈추기.
                break
        if min_danger > danger:                                # 더한 결과가 최솟값보다 작다면, 최솟값 변경하기.
            min_danger = danger

# 5. 결과 출력하기.
    print(f'#{tc+1}', min_danger)