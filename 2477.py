from collections import deque


def find_wallet():
    cnt_fns = cnt_ans = 0
    
    reception_waiting = deque()
    reception_desk = []
    for desk in a_list:
        reception_desk.append([desk])
    print(reception_desk)
    repair_waiting = deque()
    repair_desk = []
    for desk in b_list:
        reception_desk.append([desk])
    
    rct_cnt = rqr_cnt = 0
    t = 0
    while True:
        print(f'=========================={t}==========================')
        if cnt_fns == K:
            break
        
        for desk in reception_desk:
            if len(desk) > 1:
                if desk[1] == desk[2]:
                    desk.pop()
                    desk.pop()
                    rct_cnt -= 1
                    print('pop', reception_waiting, reception_desk)

        while t_deque[0] == t:
            customer = t_deque.popleft()
            reception_waiting.append(customer)
        print(reception_waiting, reception_desk)
        
        
        
        if rct_cnt < N and reception_waiting:
            while reception_waiting and rct_cnt != N:
                for desk in reception_desk:
                    if reception_waiting and len(desk) == 1 and rct_cnt < N:
                        reception_waiting.popleft()
                        desk.extend([t, t+desk[0]])
                        rct_cnt += 1
        print(reception_waiting, reception_desk)
        
        
        if t == 2 : break
                        
        t += 1
        for desk in reception_desk:
            if len(desk) > 1:
                desk[1] += 1
    return cnt_ans
        

T = int(input())
for tc in range(T):
    N, M, K, A, B = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    t_deque = deque(map(int, input().split()))
    
    find_wallet()