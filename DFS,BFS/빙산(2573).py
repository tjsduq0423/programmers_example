from collections import deque

n, m = map(int, input().split())
ocean = [list(map(int, input().split())) for _ in range(n)]


def is_separated(ocean, years):
    visited = [[True] * m for _ in range(n)]
    steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(n):
        for j in range(m):
            if ocean[i][j] == 0:
                visited[i][j] = False
    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                cnt += 1  # 덩어리 갯수
                if cnt >= 2:
                    return years
                queue = deque([(i, j)])

                while queue:  # bfs
                    x, y = queue.popleft()

                    for dx, dy in steps:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
                            queue.append((nx, ny))
                            visited[nx][ny] = False
    if cnt == 0:
        return 0
    return is_separated(melt(ocean), years + 1)


def melt(ocean):
    steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    melted_ocean = [[0] * m for _ in range(n)]  # 녹이고 난 바다

    for i in range(n):
        for j in range(m):
            if ocean[i][j] != 0:  # ice 녹이기
                zero_cnt = 0  # 인접 바다의 개수
                for di, dj in steps:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and ocean[ni][nj] == 0:
                        zero_cnt += 1
                melted_ocean[i][j] = (
                    0 if zero_cnt > ocean[i][j] else ocean[i][j] - zero_cnt
                )
    return melted_ocean


print(is_separated(ocean, 0))
