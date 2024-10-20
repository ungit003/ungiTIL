def finder(x, y, z):
    global ans
    X, Y, Z = x**2, y**2, z**2
    if X == Y + Z:
        ans = 'right'
    elif Y == Z + X:
        ans = 'right'
    elif Z == X + Y:
        ans = 'right'


while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    ans = 'wrong'
    finder(a, b, c)
    print(ans)
