# def finding(P, low, high, Pn):
#     global count
#     count +=1
#
#     if low > high:
#         return False
#
#     mid = (low + high) // 2
#     if Pn == P[mid]:
#         return True
#     elif Pn < P[mid]:
#         return finding(P, low, mid-1, Pn)
#     elif Pn > P[mid]:
#         return finding(P, low+1, high, Pn)
#
# count = 0

# if finding(P, 0, P-1, Pa) == True:
#     print(count)
T = int(input())
for tc in range(T):
    P, Pa, Pb = map(int, input().split())

    low = 1
    high = P
    count = 0
    while True:
        count += 1
        mid = int((high + low)/2)

        if mid == Pa:
            break
        elif mid > Pa:
            high = mid
        elif mid < Pa:
            low = mid

    Pa_count = count

    low = 1
    high = P
    count = 0
    while True:
        count += 1
        mid = int((high + low)/2)

        if mid == Pb:
            break
        elif mid > Pb:
            high = mid
        elif mid < Pb:
            low = mid

    Pb_count = count

    if Pa_count > Pb_count:
        print(f'#{tc+1} B')
    if Pa_count == Pb_count:
        print(f'#{tc+1} 0')
    if Pa_count < Pb_count:
        print(f'#{tc+1} A')


# 보간 한 경우

T = int(input())
for tc in range(T):
    P, Pa, Pb = map(int, input().split())

    low = 1
    high = P
    count = 0
    while True:
        count += 1
        mid = int((high + low)/2)

        if mid == Pa:
            break
        elif mid > Pa:
            high = mid-1
        elif mid < Pa:
            low = mid+1

    Pa_count = count

    low = 1
    high = P
    count = 0
    while True:
        count += 1
        mid = int((high + low)/2)

        if mid == Pb:
            break
        elif mid > Pb:
            high = mid-1
        elif mid < Pb:
            low = mid+1

    Pb_count = count

    if Pa_count > Pb_count:
        print(f'#{tc+1} B')
    if Pa_count == Pb_count:
        print(f'#{tc+1} 0')
    if Pa_count < Pb_count:
        print(f'#{tc+1} A')