def solution(sizes):
    m, n = 0, 0

    for [x, y] in sizes:
        bigger = max(x, y)
        smaller = min(x, y)
        m = max(m, bigger)
        n = max(n, smaller)

    return m * n

    """
    def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
    
    """
