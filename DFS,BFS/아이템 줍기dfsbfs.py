from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    visited = [[True] * 102 for _ in range(102)]
    start = (2 * characterX, 2 * characterY)
    end = (2 * itemX, 2 * itemY)

    # 사각형 전체 칠하기
    for [x, y, X, Y] in rectangle:
        for x_p in range(2 * x, 2 * X + 1):
            for y_p in range(2 * y, 2 * Y + 1):
                visited[x_p][y_p] = False

    # 사각형 내부 덜어내기 - 모든 사각형을 겹쳐 그린 상태에서 내부만 덜어내면 외각선만 False 값을 가짐
    for [x, y, X, Y] in rectangle:
        for x_p in range(2 * x + 1, 2 * X):
            for y_p in range(2 * y + 1, 2 * Y):
                visited[x_p][y_p] = True

    steps = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visited[start[0]][start[1]] = 0
    queue = deque([start])

    # bfs 시작
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return visited[x][y] // 2

        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 102 and 0 <= ny < 102 and visited[nx][ny] == False:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return -1


solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8)
