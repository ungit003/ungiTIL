"""
칸토어 집합은 0과 1사이의 실수로 이루어진 집합으로, 구간 [0, 1]에서 시작해서 각 구간을 3등분하여 가운데 구간을 반복적으로 제외하는 방식으로 만든다.

전체 집합이 유한이라고 가정하고, 다음과 같은 과정을 통해서 칸토어 집합의 근사를 만들어보자.

1. -가 3N개 있는 문자열에서 시작한다.

2. 문자열을 3등분 한 뒤, 가운데 문자열을 공백으로 바꾼다. 이렇게 하면, 선(문자열) 2개가 남는다.

3. 이제 각 선(문자열)을 3등분 하고, 가운데 문자열을 공백으로 바꾼다. 이 과정은 모든 선의 길이가 1일때 까지 계속 한다.

예를 들어, N=3인 경우, 길이가 27인 문자열로 시작한다.

---------------------------
여기서 가운데 문자열을 공백으로 바꾼다.

---------         ---------
남은 두 선의 가운데 문자열을 공백으로 바꾼다.

---   ---         ---   ---
한번 더

- -   - -         - -   - -
모든 선의 길이가 1이면 멈춘다. N이 주어졌을 때, 마지막 과정이 끝난 후 결과를 
"""
def cantor(n):
    global ans
    if n == 0:
        ans += '-'
        return
    else:
        cantor(n-1)                     # 왼쪽 부분
        ans += ' ' * (3 **(n - 1))      # 가운데 부분
        cantor(n-1)                     # 오른쪽 부분


N = int(input())
ans = ''
cantor(N)
print(ans)


"""이건 되는데 왜 되는지 이해가 안됨."""
# from sys import stdin

# input = stdin.readline

# def cantor(n):
#     if n == 1:
#         return "-"

#     cantor_unit = cantor(n // 3)
#     cantor_res = cantor_unit + " " * (n // 3) + cantor_unit

#     return cantor_res


# while True:
#     try:
#         N = int(input())
#         print(cantor(3**N))
#     except:
#         break