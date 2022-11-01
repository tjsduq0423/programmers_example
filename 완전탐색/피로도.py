def solution(k, dungeons, n=0):
    m = [n]
    for i in range(len(dungeons)):
        if k >= dungeons[i][0]:
            updated_dungeons = [d for d in dungeons[:i]] + [
                d for d in dungeons[i + 1 :]
            ]
            m.append(solution(k - dungeons[i][1], updated_dungeons, n + 1))

    return max(m)


answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer
