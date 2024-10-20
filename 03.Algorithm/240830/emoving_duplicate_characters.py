"""
문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데,
만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.
반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.

다음은 CAAABBA에서 반복문자를 지우는 경우의 예이다.

CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.
CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.
CAA 연속 문자 AA를 지운다.
C 1글자가 남았으므로 1을 리턴한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤ 50
다음 줄부터 테스트 케이스의 별로 길이가 1000이내인 문자열이 주어진다.


[출력]
#과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다.

"""

'''
+
1. 특정 문장이 되면 이벤트 발생
2. 지우면 안되는 글자 또는 변형
3. 두개를 초과하는 글자에 대한 처리방법
4. 글자가 쌍을 이루었을때만 지워지도록 a+b, b+i+n+g+o, ~~~
'''

'''
문자열 s에서 조건에 맞게 반복문자를 지우려고 한다. 지워진 부분은 다시 앞 뒤를 연결한다.
만약에 다시 조건에 맞는 반복문자가 생기면 이 부분을 다시 지운다. 
반복문자를 지울 때 마다 점수를 1점씩 획득한다고 할 때, 반복문자를 지운 후 점수를 출력하시오.

-조건-
1. 같은 문자가 두 개 연결되어 있으면 문자열에서 지울 수 있다.
2. 알파벳 순서대로 두 개가 연속되면 문자열에서 지울 수 있다. Z 다음에는 A가 오지 않는다.
3. 세 개 이상의 문자가 연결되어 있으면 지울 수 없다.
4. 세 개 이상의 알파벳이 연속되면 지울 수 없다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1 ≤ T ≤ 50
다음 줄부터 테스트 케이스의 별로 길이가 1000이내인 문자열이 주어진다.


[출력]
#과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다.
'''
# def erasing(s, cnt):
#     for i in range(len(s) - 3):
#         finder = s[i:i + 4]
#         if finder[1] == finder[2]:
#             if finder[0] != finder[1] and finder[2] != finder[3]:
#                 s = s[:i + 1] + s[i + 3:]
#                 cnt += 1


T = int(input())
for tc in range(T):
    words = '0' + input() + '0'

    # print(words)
    cnt = 0
    exist = False

    while not exist:

        # print(len(words))
        if len(words) < 4:
            break

        # print(len(words), words)
        for k in range(1, len(words) - 2):
            if k + 1 >= len(words):
                continue
            if words[k] == words[k + 1] or ord(words[k]) + 1 == ord(words[k + 1]):
                for i in range(len(words) - 3):
                    finder = words[i:i + 4]

                    if finder[1] == finder[2]:
                        if finder[0] != finder[1] and finder[2] != finder[3]:
                            words = words[:i + 1] + words[i + 3:]
                            cnt += 1
                            break

                    if ord(finder[1]) + 1 == ord(finder[2]):
                        if ord(finder[0]) + 1 != ord(finder[i]) and ord(finder[2]) + 1 != ord(finder[3]):
                            words = words[:i + 1] + words[i + 3:]
                            cnt += 1
                            break

        exist = True

    print(words, cnt)

# def process_string(s):
#     cnt = 0
#     while True:
#         i = 0
#         n = len(s)
#         removed = False
#
#         while i < n - 1:
#             # Check for repeated characters
#             if s[i] == s[i + 1]:
#                 s = s[:i] + s[i + 2:]
#                 cnt += 1
#                 removed = True
#                 n = len(s)
#                 i = max(i - 1, 0)  # Move back to handle overlapping cases
#             # Check for consecutive alphabetical characters
#             elif i < n - 2 and ord(s[i]) + 1 == ord(s[i + 1]) and ord(s[i + 1]) + 1 == ord(s[i + 2]):
#                 s = s[:i] + s[i + 3:]
#                 cnt += 1
#                 removed = True
#                 n = len(s)
#                 i = max(i - 1, 0)  # Move back to handle overlapping cases
#             else:
#                 i += 1
#
#         if not removed:
#             break
#
#     return cnt
#
#
# # Read number of test cases
# T = int(input())
# for tc in range(1, T + 1):
#     s = input().strip()
#     score = process_string(s)
#     print(f"#{tc} {score}")