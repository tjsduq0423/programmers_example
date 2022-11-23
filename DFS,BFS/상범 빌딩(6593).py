from collections import deque


def BFS(building, start, end, l, r, c):
    steps = [(0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
    queue = deque([start])
    cnt = 0
    while queue:
        q_len = len(queue)
        while q_len > 0:
            i, j, k = queue.popleft()
            if (i, j, k) == end:
                return "Escaped in " + str(cnt) + " minute(s)."
            for di, dj, dk in steps:
                ni, nj, nk = i + di, j + dj, k + dk
                if (
                    0 <= ni < l
                    and 0 <= nj < r
                    and 0 <= nk < c
                    and building[ni][nj][nk] != "#"
                ):
                    queue.append((ni, nj, nk))
                    building[ni][nj][nk] = "#"
            q_len -= 1
        cnt += 1
    return "Trapped!"


answer = []
while True:
    l, r, c = map(int, input().split(" "))
    if (l, r, c) == (0, 0, 0):
        break

    building = []
    for i in range(l):
        temp1 = []
        for j in range(r + 1):
            temp2 = list(input())
            if j == r:
                break
            for k in range(c):
                if temp2[k] == "S":
                    s_location = (i, j, k)
                    temp2[k] = "#"
                if temp2[k] == "E":
                    e_location = (i, j, k)
            temp1.append(temp2)
        building.append(temp1)
    answer.append(BFS(building, s_location, e_location, l, r, c))

for a in answer:
    print(a)
