def inorder(node):
    # print(node)
    left, right = node[2], node[3]
    # print(left, right)
    if node[2]:
        # print('L')
        inorder(arr[left])
    if node[3]:
        # print('R')
        inorder(arr[right])
    if not node[1].isdecimal():
        # print('y')
        # equ = ''
        # equ += str(arr[left][1])
        # equ += node[1]
        # equ += str(arr[right][1])
        cl, cr = float(arr[left][1]), float(arr[right][1])
        if node[1] == '+':
            equ = cl + cr
        if node[1] == '-':
            equ = cl - cr
        if node[1] == '*':
            equ = cl * cr
        if node[1] == '/':
            equ = cl / cr
        # print(equ)
        node[1] = str(equ)
    return node[1]


T = 10
for tc in range(T):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    for elem in arr:
        if len(elem) != 4:
            while len(elem) != 4:
                elem += ['0']
        for i in range(2, len(elem)):
            if elem[i].isdecimal():
                elem[i] = int(elem[i])

    arr.insert(0, [0, 0, 0, 0])
    # print(arr)
    ans = inorder(arr[1])
    cutting = []
    for i in range(len(str(ans))):
        cutting.append(str(ans)[i])
    res = ''.join(cutting[:-2])
    # print(cutting)
    # print(res)
    print(f'#{tc+1} {res}')
