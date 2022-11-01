def solution(brown, yellow):
    div = [
        (i, (brown + yellow) // i)
        for i in range(1, (brown + yellow) + 1)
        if (brown + yellow) % i == 0 and i >= ((brown + yellow) // i)
    ]

    for d in div:
        if brown // 2 + 2 == d[0] + d[1]:
            return [d[0], d[1]]
    # row + col == brown//2 + 2
    # row * col == brown + yellow


def solution(brown, yellow):
    equation_a = (brown + 4) // 2
    equation_b = brown + yellow

    for i in range(3, 2000):
        for j in range(3, 2000):
            if (i + j > equation_a) or (i * j > equation_b):
                break
            if (i + j == equation_a) and (i * j == equation_b):
                return [j, i]
