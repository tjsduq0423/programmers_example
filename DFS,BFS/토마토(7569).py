import sys
from collections import deque

input = sys.stdin.readline

n, m, h = map(int, input().split(" "))

steps = [(0, 0, 1), (0, 1, 0), (0, -1, 0), (0, 0, -1), (-1, 0, 0), (1, 0, 0)]
visited = [[[False] * n for _ in range(m)] for _ in range(h)]
tomato_queue = deque([])
tomatoes = []

for i in range(h):
    temp1 = []
    for j in range(m):
        temp2 = list(map(int, input().split(" ")))
        temp1.append(temp2)
        for k in range(n):
            if temp2[k] == 1:
                tomato_queue.append((i, j, k))
                visited[i][j][k] = True
            if temp2[k] == -1:
                visited[i][j][k] = True
    tomatoes.append(temp1)


def BFS():
    cnt = 0
    while tomato_queue:
        tomato_queue_length = len(tomato_queue)
        while tomato_queue_length > 0:
            x, y, z = tomato_queue.popleft()
            for dx, dy, dz in steps:
                nx, ny, nz = x + dx, y + dy, z + dz
                if (
                    0 <= nx < h
                    and 0 <= ny < m
                    and 0 <= nz < n
                    and not visited[nx][ny][nz]
                ):
                    tomato_queue.append((nx, ny, nz))
                    visited[nx][ny][nz] = True
            tomato_queue_length -= 1
        cnt += 1

    if len(set(sum(sum(visited, []), []))) == 1:
        return cnt - 1
    return -1


print(BFS())
