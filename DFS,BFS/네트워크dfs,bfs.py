from collections import deque


def solution(n, computers):
    answer = 0
    queue = deque([])
    visited = [False] * n

    for i in range(n):
        if visited[i] == True:
            continue
        visited[i] = True
        queue.append(i)
        answer += 1

        while queue:
            cur = queue.popleft()

            for idx, computer in enumerate(computers[cur]):
                if not visited[idx] and computer == 1:
                    queue.append(idx)
                    visited[idx] = True

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
