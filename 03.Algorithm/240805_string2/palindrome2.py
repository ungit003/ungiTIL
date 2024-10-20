import sys
sys.stdin = open("palindrome2.txt", "r")

T = 10
N = 100
for _ in range(T):
    tc = int(input())
    words = [input() for _ in range(N)]

    print(words)
    print('-' * 100)

    word_len = 1
    for elem in words:
        for stt in range(len(elem)):
            for i in range(len(elem) - stt):
                check_word = elem[stt:stt + i]
                if check_word == check_word[::-1]:
                    if len(check_word) > 1:
                        word_len = len(check_word)
    print(word_len)