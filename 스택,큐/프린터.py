from collections import deque


def solution(priorities, location):
    answer = 0
    priorities = deque([(i, p) for i, p in enumerate(priorities)])
    while priorities:
        idx, priority = priorities.popleft()
        for i,pr in priorities:
            if priority <  pr:
                priorities.append((idx, priority))
                break
        else:
            if idx == location:
                return answer + 1
            else:
                answer += 1
    return answer