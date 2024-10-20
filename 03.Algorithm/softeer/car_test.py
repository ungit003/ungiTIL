"""
문제점.
시간 초과

이유.
리스트 in 연산은 속도가 느려질 수 있음. -> set 을 쓸 것

index 연산이 느림 -> 인덱스를 미리 저장. 어디에? dict

문제의 입력 범위와 쿼리 수에 따라 더 최적화 할 수 있다 ?
"""

n, q = map(int, input().split())
cars = list(map(int, input().split()))
expect = [int(input()) for _ in range(q)]

car_set = set(cars)

cars.sort()
# print(cars)
# car_index = {car: idx for idx, car in enumerate(cars)}
car_index = {}
for i in range(n):
    car_index[cars[i]] = i

print(car_index)

for elem in expect:
    # print(elem)
    if elem in car_set:
        # print('case1')
        finder = car_index[elem]
        if finder == 0 or finder == n-1:
            print(0)
        else:
            left = finder
            right = n-1 - finder
            print(left * right)
    else:
        # print('case2')
        print(0)

'''
    문제의도 = 이분탐색 사용해라!

    같은말임



    받은 배열 한번 정렬 - N logN (어짜피 처음에 한번하고 반복안해서 시간 상관 X)


    바로 q번 반복해서 답찾는다고 가정
        이진탐색을하면서 나보다 작은애들 몇개 있는지 찾기(logN)

처음에 정렬한다고 NlogN 한번 하고

for문 q번 반복 20만번
    logN번 = 16번


=> 80만번 + 320만번

    100

    37
    100 1~50 51~ 100


100개
정렬-> 인덱스가 나온다 이말 아님?

37번에 대해서 조사
앞에 36개 아님? 복잡도 1 아님?

1 3 5 7 8 9
'''