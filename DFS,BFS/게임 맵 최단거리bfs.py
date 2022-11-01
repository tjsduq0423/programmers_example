from collections import deque


def solution(maps):
    steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 상하 좌우 움직임
    queue = deque([(0, 0)])  # maps 에서의 시작 위치를 큐에 삽입

    while queue:  # bfs
        x, y = queue.popleft()

        # 도착 조건에서 maps에 기록하면서 온 진행 횟수 return
        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            return maps[x][y]

        # 진행 가능한 모든 방향에대해 진행 하게되면 maps에 +1 을 통해 기록하고 진행한 노드를 큐에 삽입
        for step in steps:
            nx, ny = x + step[0], y + step[1]

            # 맵을 벗어나지 않고 진행가능하며 방문하지 않은 노드 maps에서 값이 1인 노드
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    # bfs 가 끝났는데 조건에 도달하지 못한경우 = 막혀 있음 -1 리턴
    return -1
