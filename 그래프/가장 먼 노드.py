from collections import defaultdict
from collections import deque


def solution(n, edge):
    terminal_distance = []  # 말단 노드에 대한 거리 저장 배열
    graph = defaultdict(list)

    for i in edge:  # 그래프 생성
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    visited = [False] * (n + 1)  # n 번 노드에 대한 방문 확인 배열
    queue = deque([(1, 0)])  # init
    visited[1] = True  # 1번 노드가 시작 노드

    while queue:  # BFS
        node, cnt = queue.popleft()

        # 말단 노드인지 확인 - 말단 노드라면 cnt(1번 노드로부터의 거리)를 terminal_distance에 저장
        for next in graph[node]:
            if visited[next] == False:
                break
        else:
            terminal_distance.append(cnt)
            continue

        for next in graph[node]:  # 말단 노드가 아니라면 인접 노드 방문처리후 큐에 삽입
            if visited[next] == False:
                queue.append((next, cnt + 1))
                visited[next] = True

    # BFS를 마치고 말단 노드의 최대값의 개수를 구해 return
    return terminal_distance.count(max(terminal_distance))
