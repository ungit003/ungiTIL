T = int(input())
for tc in range(T):
    case = input()
    # a = case.split('()')
    b = case.replace('()', '0')
    c = b.replace('(', ' |-')
    d = c.replace(')', '-| ')
    e = len(d)
    # print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print('-' * 50)