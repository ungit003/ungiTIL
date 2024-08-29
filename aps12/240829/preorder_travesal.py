def pre_order(t):
    if t:
        print(t, end=' ')
        pre_order(left[t])
        pre_order(right[t])


N = int(input())
nums = list(map(int, input().split()))

nodes = []
for i in range(0, len(nums), 2):
    nodes.append([nums[i], nums[i + 1]])
print(nodes)

left = [0] * (N + 1)
right = [0] * (N + 1)
par = [0] * (N + 1)

for i in range(N - 1):
    p, c = nums[i * 2], nums[i * 2 + 1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p

print(left)
print(right)
print(par)

c = N
while par[c] != 0:
    c = par[c]
root = c
print(root)
pre_order(root)
