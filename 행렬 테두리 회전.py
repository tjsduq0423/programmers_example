def solution(rows, columns, queries):
    result = []
    board = [[columns * row + col + 1 for col in range(columns)] for row in range(rows)]

    for x1, y1, x2, y2 in queries:
        x1, x2, y1, y2 = x1 - 1, x2 - 1, y1 - 1, y2 - 1
        edge_nodes = []

        for y in range(y1, y2 + 1):
            if board[x1][y] not in edge_nodes:
                edge_nodes.append((x1, y))

        for x in range(x1 + 1, x2 + 1):
            if board[x][y2] not in edge_nodes:
                edge_nodes.append((x, y2))

        for y in range(y2 - 1, y1 - 1, -1):
            if board[x2][y] not in edge_nodes:
                edge_nodes.append((x2, y))

        for x in range(x2 - 1, x1, -1):
            if board[x][y1] not in edge_nodes:
                edge_nodes.append((x, y1))

        value_arr = [board[x][y] for x, y in edge_nodes]

        result.append(min(value_arr))

        value_arr = value_arr[-1:] + value_arr[:-1]

        for v, (x, y) in zip(value_arr, edge_nodes):
            board[x][y] = v

    return result


""" 
    하나하나 계산하는 방식이 아슬아슬하게 테스트를 통과하기 때문에 큐와 스택같은 자료구조를 활용하는 게좋다
    from collections import deque


    def solution(rows, columns, queries):
        arr = [[i+columns*j for i in range(1,columns+1)] for j in range(rows)]
        answer, result = deque(), []
        for i in queries:
            a,b,c,d = i[0]-1,i[1]-1,i[2]-1,i[3]-1
            for x in range(d-b):
                answer.append(arr[a][b+x])
            for y in range(c-a):
                answer.append(arr[a+y][d])
            for z in range(d-b):
                answer.append(arr[c][d-z])
            for k in range(c-a):
                answer.append(arr[c-k][b])
            answer.rotate(1)
            result.append(min(answer))
            for x in range(d-b):
                arr[a][b+x] = answer[0]
                answer.popleft()
            for y in range(c-a):
                arr[a+y][d] = answer[0]
                answer.popleft()
            for z in range(d-b):
                arr[c][d-z] = answer[0]
                answer.popleft()
            for k in range(c-a):
                arr[c-k][b] = answer[0]
                answer.popleft()
    return result


"""
