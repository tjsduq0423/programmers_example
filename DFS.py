"""
    DFS 는 깊이 우선 탐색으로 그래프에서 깊ㅇ은 부분을 우선적으로 탐색하는 알고리즘
    DFS 는 스택 자료구조(혹은 재귀한수)를 이용하며, 구체적으로는
    1. 탐색 시작 노드를 스택에 삽입, -방문처리-
    2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리, 방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 pop
    3. 더이상 2번의 과정을 수행할 수 없을 때까지 반복
"""
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
    
visited = [False] * 9

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end= ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)


