"""
문제 요약
"""
from collections import deque


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    nums = deque(input())
    # print(nums)

    cnt = 0
    codes = set()
    while True:
        if cnt == N//4:
            # print('end')
            break
        # print('c', cnt, nums)

        if cnt:
            # print('need pop')
            x = nums.popleft()
            nums.append(x)
            # print('a', nums)

        for i in range(4):
            hex_code = list(nums)[N//4*i:N//4*(i+1)]
            code = int(''.join(hex_code), 16)
            codes.add(code)
        # print(codes)
        # print(nums)
        cnt += 1

    ans = list(codes)
    ans.sort(reverse=True)
    print(f'#{tc+1}', ans[K-1])
