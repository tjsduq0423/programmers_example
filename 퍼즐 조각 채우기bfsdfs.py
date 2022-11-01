from collections import deque


def rotate_90(board):
    n = len(board)
    rotated_board = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            rotated_board[col][n - 1 - row] = board[row][col]

    return rotated_board


def compare(piece, blank):
    temp = [(x - i, y - j) for (x, y), (i, j) in zip(piece, blank)]
    if len(set(temp)) == 1:
        return True
    return False


def solution(game_board, table):
    answer = 0
    pieces = []
    N = len(game_board)
    steps = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    for x in range(N):
        for y in range(N):
            if table[x][y] == 1:
                piece = []
                table[x][y] = 0
                queue = deque([(x, y)])

                while queue:
                    r, c = queue.popleft()
                    piece.append((r, c))

                    for dx, dy in steps:
                        nr, nc = r + dx, c + dy
                        if ((0 <= nr < N) and (0 <= nc < N) and (table[nr][nc])) == 1:
                            table[nr][nc] = 0
                            queue.append((nr, nc))

                pieces.append(piece)
    pieces.sort(key=lambda x: len(x))

    for i in range(4):  # game_board 90도 회전
        for x in range(N):
            for y in range(N):
                if game_board[x][y] == 0:
                    blank = []
                    game_board[x][y] = 1
                    queue = deque([(x, y)])

                    while queue:
                        r, c = queue.popleft()
                        blank.append((r, c))

                        for dx, dy in steps:
                            nr, nc = r + dx, c + dy
                            if (
                                (0 <= nr < N)
                                and (0 <= nc < N)
                                and (game_board[nr][nc] == 0)
                            ):
                                game_board[nr][nc] = 1
                                queue.append((nr, nc))

                    for piece in pieces:

                        if len(piece) == len(blank) and compare(piece, blank):
                            pieces.remove(piece)
                            answer += len(blank)
                            print(i, blank, piece, answer)
                            break
                    else:
                        for x, y in blank:
                            game_board[x][y] = 0

        game_board = rotate_90(game_board)

    return answer


solution([[0, 0, 0], [0, 1, 1], [0, 1, 1]], [[1, 1, 0], [1, 1, 0], [0, 0, 0]])
