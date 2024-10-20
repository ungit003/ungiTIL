"""
풀이 전략
1. 행에 대해서 차례대로 조사.
2. 높이가 달라지는 부분을 앞 뒤로 인덱스를 뽑음 2 2 3 이면 [1, 2]
2-1. 만약 높이가 달라진 크기가 1보다 크면 종료
3. 경사로를 놓을 수 있는지 검사.
3-1. 낮은 곳 기준으로 경사로 길이만큼 칸이 있는지.
3-2 낮은 곳 기준으로 경사로 길이만큼 값이 같은지.
4. 경사로를 놓을 수 있다면 카운트 + 1
5. 행, 열 뒤집어서 한 번 더

또는.
1 1 2 2 3 4 라고 쳐보자. 경사로 길이는 2
가장 낮은 값은 1인데, 여기서 2로 올라가야함.
2랑 인접한 1 기준으로 두칸이 있음.
그러면 1을 전부다 2로 올림.
2 2 2 2 3 4가 됨
이걸 반복하면
3 3 3 3 3 4
4 4 4 4 4 4 로 됨
이러면 + 1

또는
한 행에 대해서
1 1 2 2 3 3 4 3 3 3 2 2 2 2 3 3 이라고 쳐보자. 경사로 길이는 2
앞에서부터 stack에 쌓음.
최초에 값을 넣고. 그 값과 같으면 그대로 넣어줌
만약에 값이 다르다면. 클 때와 작을 때 구분
1. 클 때
우선. 값의 차이가 1보다 크면 멈춤
1차이라면 들어있는 1의 갯수를 조사.
경사로의 길이보다 크거나 같으면 2를 넣어줌 아니면 멈춤
1 1 2 2 3 3 4까지 옴
2. 작을 때
경사로의 길이만큼 값을 가져옴. 3앞 3뒤 가 되겠지?
이 값들이 모두 4보다 1만큼 작은 수이면 스택에 넣음 <- 기술적으로 가능할까
그럼 1 1 2 2 3 3 4 3 3 3 2 2 2 2 3 3
스택의 길이가 N이 되면. 카운트 + 1
"""


def searching(line):
    global cnt
    stk = []
    cannot_use = set()
    stk.append(line[0])  # 하나 넣고 시작
    for i in range(1, N):
        # 같을 때
        if stk[-1] == line[i]:
            stk.append(line[i])
            print(stk, '=')
        # 높아질 때
        elif stk[-1] < line[i]:
            if line[i] - stk[-1] > 1:
                print('b1')
                break
            if len(stk) < X:
                print('b2')
                break
            check_bridge = set()
            for x in range(X):
                check_bridge.add(i - 1 - x)
            lcn = len(cannot_use)
            lcb = len(check_bridge)
            cannot_use = cannot_use | check_bridge
            lsm = len(cannot_use)
            if lcn + lcb != lsm:
                print(lcn, lcb, lsm)
                break
            stk = [line[i]] * (len(stk) + 1)
            print(stk, '<')
        # 낮아질 때
        else:
            if stk[-1] - line[i] > 1:
                print('b3')
                break
            if i + X - 1 > N - 1:
                print('b4')
                break
            check = []
            for x in range(X):
                check.append(line[i + x])
            print(check)
            if len(set(check)) > 1:
                print('b5')
                break
            check_bridge = set()
            for x in range(X):
                check_bridge.add(i + x)
            lcn = len(cannot_use)
            lcb = len(check_bridge)
            cannot_use = cannot_use | check_bridge
            lsm = len(cannot_use)
            if lcn + lcb != lsm:
                print(lcn, lcb, lsm)
                break
            stk = [line[i]] * (len(stk) + 1)
            print(stk, '>')
    print(len(stk))
    print()
    if len(stk) == N:
        cnt += 1
        print(cnt)


def transpose(m):
    for i in range(N):
        for j in range(N):
            if i > j:
                m[i][j], m[j][i] = m[j][i], m[i][j]


T = int(input())
for tc in range(T):
    N, X = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for row in mat:
        searching(row)

    transpose(mat)
    for row in mat:
        searching(row)

    print(f'#{tc + 1}', cnt)
