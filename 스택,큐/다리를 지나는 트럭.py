from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    cur_weight = 0
    wait_queue = deque(truck_weights)
    bridge_queue =deque([0] * bridge_length)

    while wait_queue:
        q = bridge_queue.popleft()
        cur_weight -= q
        
        if cur_weight + wait_queue[0] > weight:
            bridge_queue.append(0)
        else:
            t = wait_queue.popleft()
            cur_weight += t
            bridge_queue.append(t)
        
        answer += 1
    while bridge_queue:
        q = bridge_queue.popleft()
        answer += 1
    
    return answer

# def solution(bridge_length, weight, truck_weights):
#     bridge = deque(0 for _ in range(bridge_length))
#     total_weight = 0
#     step = 0
#     truck_weights.reverse()

#     while truck_weights:
#         total_weight -= bridge.popleft()
#         if total_weight + truck_weights[-1] > weight:
#             bridge.append(0)
#         else:
#             truck = truck_weights.pop()
#             bridge.append(truck)
#             total_weight += truck
#         step += 1

#     step += bridge_length

#     return step