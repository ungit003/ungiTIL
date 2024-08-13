def solution(bridge_length, weight, truck_weight):
    bridge = []
    time = 1
    while True:
        if len(bridge) != 0:
            if bridge[0][1] == bridge_length + 1:
                bridge.pop(0)
            if len(bridge) == 0 and time != 0 and len(truck_weight) == 0:
                return time
        if len(truck_weight) != 0:
            sum_bridge = 0
            for i in range(len(bridge)):
                sum_bridge += bridge[i][0]
            if weight - sum_bridge >= truck_weight[0] and len(bridge) < bridge_length:
                # 웨이트 - 브릿지 위의 무게 합 >= 트럭무게
                bridge.append([truck_weight.pop(0), 1])
        for i in range(len(bridge)):
            bridge[i][1] += 1
        time += 1

print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))