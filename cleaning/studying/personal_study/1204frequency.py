'''
어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계 자료를 만들려고 한다.
이때, 이 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데, 
여기서 최빈수는 특정 자료에서 가장 여러 번 나타나는 값을 의미한다.
다음과 같은 수 분포가 있으면,

10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3

최빈수는 8이 된다.
최빈수를 출력하는 프로그램을 작성하여라 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).

[제약 사항]
학생의 수는 1000명이며, 각 학생의 점수는 0점 이상 100점 이하의 값이다.
 
[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄부터는 점수가 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.
'''
T = int(input())

for i in range(T) :
    test_number = int(input())
    group = list(map(int, input().split())) # 1000개
    # print(group)
    group_s = set(group) # 중복 거르기
    # print(group_s)
    set_group = list(group_s)  # 다시 리스트로 바꾸기
    # print(set_group)
    
    count_file = {}
    for j in range(len(set_group)) : # 원소 갯수만큼 반복
        count_file[j] = group.count(set_group[j])
    print(count_file, end = " ")
    
    def dict_comp(k, l) :
        global count_file
        if count_file[k] > count_file[l] :
            del count_file[l]
        elif count_file[k] == count_file[l] :
            if k > l :
                del count_file[l]

            
    print(f'#{test_number} {count_file[i]}')
# print(f'#{i+1} {count_file[i][i]} {len(group)}')

# Memory error occured, (e.g. segmentation error, memory limit Exceed, stack overflow,... etc)
# 이게 런타임 에러래

# 0 ~ 100 dict -> input 50개?씩 잘라서 카운트되면 +1? 
# value 뽑아서 list 만들고 제일 큰 값의 key 출력?

# T = int(input())
# count_file = []
# for i in range(T) :
#     group = list(map(int, input().split())) # 1000개

#     group_s = set(group)
#     set_group = list(group_s)

# for j in range(len(group_s)) :
#     group_count = []
#     group_count.append(group.count(set_group[i]))
# count_file.append(group_count)
# print(f'#{i+1} {count_file[i][i]}')