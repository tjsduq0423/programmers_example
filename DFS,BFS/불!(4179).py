import sys
from collections import deque


input = sys.stdin.readline
r, c = map(int, input().split(" "))

maze = []
steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
fire_queue = deque([])
jihoon_queue = deque([])

for i in range(r):
    temp = list(input().strip())
    maze.append(temp)
    for j, t in enumerate(temp):
        if t == "J":
            jihoon_queue.append((i, j))
        if t == "F":
            fire_queue.append((i, j))


def BFS():
    move_cnt = 0

    while jihoon_queue:
        fire_queue_length = len(fire_queue)
        while fire_queue_length > 0:
            x, y = fire_queue.popleft()
            for dx, dy in steps:
                nx, ny = x + dx, y + dy
                if (
                    (0 <= nx < r)
                    and (0 <= ny < c)
                    and maze[nx][ny] != "#"
                    and maze[nx][ny] != "F"
                ):
                    fire_queue.append((nx, ny))
                    maze[nx][ny] = "F"
            fire_queue_length -= 1

        jihoon_queue_length = len(jihoon_queue)
        while jihoon_queue_length > 0:
            x, y = jihoon_queue.popleft()
            for dx, dy in steps:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < r) or not (0 <= ny < c):
                    return move_cnt + 1
                else:
                    if maze[nx][ny] == ".":
                        jihoon_queue.append((nx, ny))
                        maze[nx][ny] = "J"
            jihoon_queue_length -= 1

        move_cnt += 1
    return "IMPOSSIBLE"


print(BFS())
