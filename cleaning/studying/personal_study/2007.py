'''
패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.

[제약 사항]
각 문자열의 길이는 30이다. 마디의 최대 길이는 10이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 길이가 30인 문자열이 주어진다.

[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''
'''
#1
# 문자를 받는다 o
# 문자를 딕셔너리에 기록한다 o
# 문자가 없으면 등록, 있으면 +1 o
# 문자를 각각 세어서 숫자를 더한다 o
# 가장 작은 밸류를 출력 o

#2
# 문자를 받는다 o
# 문자를 딕셔너리에 기록한다 o
# 문자가 없으면 등록, 있으면 +1 o
# 문자를 각각 세어서 숫자를 더한다 o
# 제일 작은 숫자로 30을 나눈 몫 출력o

T = int(input()) # 테스트 케이스

for i in range(T) : # 반복
    pattern = input() # 문자열 입력
    pat_dict = {}
    for j in range(30) :
        if pattern[j] in pat_dict :
            pat_dict[pattern[j]] += 1
        else :
            pat_dict[pattern[j]] = 1
    result = min(pat_dict.values())
    # print(pat_dict)
    # result = len(pat_dict)
    print(f'#{i+1} {30//result}')
'''
#3
# 문자를 받는다
# 문자를 슬라이스해서 같아지는 값을 찾는다
# 출력

T = int(input()) # 테스트 케이스

for i in range(T) : # 반복
    li = []
    pattern = input() # 문자열 입력
    for j in range(3,11) :
        if pattern[:j] == pattern[j:2*j] :
            li.append(j)
    k = min(li)
    print(f'#{i+1} {k}')