def inorder(node):
    global ans
    if node[2]:
        inorder(arr[node[2]])
    ans += node[1]
    if node[3]:
        inorder(arr[node[3]])


T = 10
for tc in range(T):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    for elem in arr:
        for i in range(len(elem)):
            if elem[i].isdecimal():
                elem[i] = int(elem[i])
        if len(elem) != 4:
            while len(elem) != 4:
                elem += [0]
    arr.insert(0, [0, 0, 0, 0])

    ans = ''
    inorder(arr[1])
    print(f'#{tc+1}', ans)
