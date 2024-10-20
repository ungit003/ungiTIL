# 주어진 조건에 맞게 테스트케이스 개수T, 매트릭스 크기 N, 정수Aij를 입력받는다.
T = int(input())
for tc in range(T):
    N = int(input())
    # 단 여기서 매트릭스를 입력 받을 때, 매트릭스 바깥을 0으로 둘러싸는 코드를 작성한다.
    mat = [[0] * (N + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 2)]

# 미생물이 먹은 먹이의 합을 저장하는 리스트를 만든다.
    mi_eat_list = []
    # 매트릭스 바깥에 0을 둘렀으므로, i와 j의 범위는 0~N-1이 아닌 1~N으로 변경하여 for문을 작성한다.
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # 미생물은 본인의 위치를 기준으로 상, 하, 좌, 우를 포함해 다섯칸을 먹기 때문에 그 값을 계산한다.
            mi_eat = mat[i][j] + mat[i+1][j] + mat[i-1][j] + mat[i][j+1] + mat[i][j-1]
            # 계산한 값을 리스트에 저장한다.
            mi_eat_list.append(mi_eat)

    # max 함수를 쓸 수 없기 때문에, 최댓값을 계산하기 위한 for문을 작성한다.
    # 최초에 미생물이 먹은 먹이 리스트의 첫번째 값을 최댓값이라 지정한다.
    list_max = mi_eat_list[0]
    # 미생물이 먹은 먹이의 합 리스트의 원소를 순회하면서 그 값이 최댓값보다 크다면 값을 바꾸는 식을 작성한다.
    for elem in mi_eat_list:
        if list_max < elem:
            list_max = elem

    # 문제의 조건에 맞게 테스트케이스 번호와 최대로 먹을 수 있는 값을 출력한다.
    print(f'#{tc+1}', list_max)