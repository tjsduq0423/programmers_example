import sys
from collections import deque


input = sys.stdin.readline
f, s, g, u, d = map(int, input().split(" "))

queue = deque([(s, 0)])
visited = [False] * (f + 1)
visited[s] = True

while queue:
    cur, cnt = queue.popleft()
    if cur == g:
        print(cnt)
        break
    if cur - d >= 1 and not visited[cur - d]:
        queue.append((cur - d, cnt + 1))
        visited[cur - d] = True
    if cur + u <= f and not visited[cur + u]:
        queue.append((cur + u, cnt + 1))
        visited[cur + u] = True
else:
    print("use the stairs")
