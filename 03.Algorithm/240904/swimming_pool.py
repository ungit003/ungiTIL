"""
풀이 전략
일단 첫 케이스. 연간 이용권
두번째 부터가 빡센데..
일단 세달짜리를 끊는법 11, 12월도 살 수 있는데 한달짜리보다 싸게 내놓는 미친 케이스가 있을 수 있으니 다 해볼 것.
백트래킹을 넣자면. 세달중에 하루라도 이용하는 날이 있을 때 의미가 있을 것.
123 234 345 456 567 678 789 8910 91011 101112 1112(13) 12(13)(14) 인데
하나 끊어놓고 또 세달짜리를 끊을 수도 있잖아.
visited 를 쓰는게 좋을듯.
세달, 한달 세개, 일일 세달치 이렇게 비교해야될 듯.
한달, 일일이랑 비교

만약에 다섯달이 있는데,
일 일 월3 < 월3 일 일 인 경우에는 어떡하지?
다섯개씩 끊어야되나.
일 일 월3 / 일 월3 일 / 월3 일 일 세개로 가르고
일이 앞이면 인덱스 하나 이동, 비짓 하나 추가
월3이 앞이면 인덱스 세개 이동, 비짓 세개 추가
---
그리디로 풀고 싶었는데 케이스 고려가 안됨.
완탐으로 해야될 듯.
14 = 1 + 13 = 1 + 1 + 12 = 1 + 1 + 1 + 11 = 3 + 11
대충 이런 느낌인데.. 이건 재귀인가?
그럼 세개짜리 놓는 경우를 먼저 생각하고.
4개라고 치면. 3 + 1 , 1 + 3
~ 6개부터
3 + 3
3 + 3 + 1, 3 + 1 + 3, 1 + 3 + 3
~~
1. 3이 4개 -> 3 * 4, 1 * 2 줄세우기 5^2, 3^4
2. 3이 3개 -> 3 * 3, 1 * 5 줄세우기 4^5,
3. 3이 2개 -> 3 * 2, 1 * 8 줄세우기 3^8, 9^2
4. 3이 1개 -> 3 * 1, 1 * 11 줄세우기  12
5. 3이 0개 -> 1 * 14 줄세우기 1
6. 12가 1개

"""


# def comp_3(s):
#     case1 = M3
#     case2 = M * 3
#     case3 = D * (plan[s] + plan[s+1] + plan[s+2])
#     find_m = [case1, case2, case3]
#     return min(find_m)
#
#
# def comp_5(s):
#     fir, sec, fou, fif = min(D*plan[s], M), min(D*plan[s+1], M), min(D*plan[s+2], M), min(D*plan[s+3], M)
#     print(fir, sec, fou, fif)
#     case1 = fir + sec + comp_3(s+2)
#     case2 = fir + comp_3(s+1) + fif
#     case3 = comp_3(s) + fou + fif
#
#     find_m = [case1, case2, case3]
#     print(find_m)
#     find_m.sort()
#     if find_m[0] == case3:
#         visited[s] = visited[s+1] = visited[s+2] = 1
#         print()
#         print('3', visited)
#         return comp_3(s)
#     else:
#         visited[s] = 1
#         print(fir, find_m[0])
#         print('1', visited)
#         return fir
#
#
# T = int(input())
# for tc in range(T):
#     D, M, M3, Y = map(int, input().split())
#     plan = list(map(int, input().split())) + [0, 0]
#
#     visited = [0] * 12
#     ans = 0
#     for i in range(10):
#         if plan[i] == 0:
#             visited[i] = 1
#             print('p0', visited)
#             continue
#         if visited[i] == 1:
#             print('pv', visited)
#             continue
#         ans += comp_5(i)
#     res = min(Y, ans)
#     print(f'#{tc+1}', res)


# def bind(s, arr):
#     if s == len(arr):
#         return
#     if arr[0] == 3:
#         bind(1, arr)
#     else:
#         if len(arr) >= s+1:
#             bind(s+1, arr)
#         if len(arr) >= s+2:
#             bind(s+2, arr)
#         if len(arr) >= s+3:
#             new_arr = [3] + arr[3:]
#             bind(s+1, new_arr)
#     return arr
#
#


def generate_combinations_with_sum(target_sum):
    # dp 배열 초기화
    dp = [[] for _ in range(target_sum + 1)]
    dp[0].append([])  # 총합이 0인 배열은 빈 배열 하나만 있음

    # 배열 생성
    for i in range(1, target_sum + 1):
        if i >= 1:
            for combination in dp[i - 1]:
                dp[i].append(combination + [1])
        if i >= 3:
            for combination in dp[i - 3]:
                dp[i].append(combination + [3])

    return dp[target_sum]


T = int(input())
for tc in range(T):
    D, M, M3, Y = map(int, input().split())
    plan = [0] + list(map(int, input().split())) + [0, 0]

# 사용 예시
    target_sum = 14
    result_arrays = generate_combinations_with_sum(target_sum)
    # for arr in result_arrays:
    #     print(arr)

    res = [Y]
    for array in result_arrays:
        arr = [0] + array
        # print(arr)
        ans = 0
        month = 0
        # while True:
        #     if month == 14:
        #         break
        #     if arr[month] == 1:
        #         print(month, end=' ')
        #         M1 = min(D*plan[month], M)
        #         ans += M1
        #         print(M1, ans, end=' ')
        #         month += 1
        #         print(month)
        #         print('-')
        #     if arr[month] == 3:
        #         print(month, end=' ')
        #         ans += M3
        #         print(M3, ans, end=' ')
        #         month += 3
        #         print(month)
        #         print('-')

        for i in range(1, len(arr)):
            if arr[i] == 1:
                month += 1
                M1 = min(D*plan[month], M)
                ans += M1
            if arr[i] == 3:
                month += 3
                ans += M3
        res.append(ans)
        # print(res)

    print(f'#{tc+1}', min(res))


