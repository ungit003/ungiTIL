import sys
sys.stdin = open('GNS_test_input.txt', 'r')

T = int(input())
num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(T):
    N = input()
    nums = input().split()

    count_list = []
    for num in num_list:
        counting = nums.count(num)
        count_list.append(counting)
=
    ans_a = []
    for i in range(10):
        a = [num_list[i]] * count_list[i]
        b = ' '.join(a)
        ans_a.append(b)
    ans_b = ' '.join(ans_a)
    print(f'#{tc+1}')
    print(ans_b)