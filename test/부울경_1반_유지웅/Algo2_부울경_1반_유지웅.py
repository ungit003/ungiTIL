# 오르막을 찾는 함수를 정의한다.
def find_up(list):
    # 반복문 안의 리스트를 사용하기 위해 글로벌로 정의한다.
    global up_list
    # 인덱스가 꼬이는 것을 방지하기 위해서 뒤에서부터 for문을 순회한다.
    for i in range(len(list) - 1, 0, -1):
        # 이전의 값이 지금의 값보다 높다면, 지금까지의 리스트를 슬라이싱해서 오르막 리스트에 넣는다.
        if list[i] < list[i - 1]:
            up_part = list[i:]
            up_list.append(up_part)
            # 그리고 남은 리스트를 새로 정의하고, 그 길이가 0이 아니라면 다시 함수에 대입되게 한다.
            new_list = list[:i]
            if len(new_list) != 0:
                return find_up(new_list)
    # 마지막에 남는 값이 존재할 때, 그 값들은 오르막 뿐임으로 그 값 또한 오르막 리스트에 넣는다.
    up_list.append(list)


# 주어진 조건에 맞게 테스트케이스 개수T, 등산로의 길이 N, 자연수 Ai를 mount 리스트에 입력받는다.
T = int(input())
for tc in range(T):
    N = int(input())
    mount = list(map(int, input().split()))
    # 함수의 결과를 입력받을 리스트를 정의하고, 실행시켜 오르막 리스트를 만든다.
    up_list = []
    find_up(mount)

    # 오르막은 두칸부터 정의됨으로, 길이가 하나인 리스트는 제거한다.
    for elem in up_list:
        if len(elem) == 1:
            up_list.remove(elem)

    # 자연수의 최댓값은 100, 등산로의 최소길이는 5 임으로 각도의 경사 최댓값을 20으로 잡는다.
    # 또한 경사로의 최솟값도 0으로 잡는다.
    min_degree = 20
    min_deg_dist = 0
    # 오르막길 리스트는 2중 리스트로 작성되어 있음으로, 각 요소를 불러온다.
    for i in range(len(up_list)):
        # 불러온 요소에서 마지막과 처음값의 차로 높이를 구하고, 그 길이로 나눠 경사도를 구한다.
        degree = (up_list[i][-1] - up_list[i][0]) / len(up_list[i])
        # 경사도가 최소일 때의 길이를 구하기 위해 앞서 지정한 두 변수에 값을 저장한다.
        if min_degree > degree:
            min_degree = degree
            min_deg_dist = len(up_list[i])

    # 오르막이 없으면 경사도가 0임을 상정하여 출력값이 0이 되게 한다.
    if min_degree == 0:
        print(f'#{tc+1}', 0)
    # 이외에는 테스트 케이스와 오르막의 길이가 출력되도록 한다.
    else:
        print(f'#{tc+1} {min_deg_dist}')









