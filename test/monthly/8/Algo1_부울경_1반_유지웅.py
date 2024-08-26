# 1. 입력값 받기.
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

# 2. 최초의 미생물 에너지, 인덱스 정의.
    energy = 0
    i = 0

# 3. 한 칸씩 진행하는 while 문 작성.
    while True:
        if i == N - 1:                          # 미생물이 끝에 도달하면 정지.
            # print('end')
            break
        else:                                   # 끝이 아닐 경우.
            if arr[i] == 1:                     # 먹이가 있다면, 에너지를 K로 충전.
                energy = K
                # print('charge')
            else:                               # 먹이가 없다면, 에너지를 1 소모.
                energy -= 1
                # print('work')

        if energy <= 0:                         # 에너지가 0 이하가 되면 멈춤.
            # print('die')
            break
        i += 1                                  # 다음 칸으로 전진.

# 4. 결과 출력.
    print(f'#{tc+1} {i+1}')                     # 인덱스 -> 좌표로 변경