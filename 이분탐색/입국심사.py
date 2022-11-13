def solution(n, times):
    low = 0
    high = 1024

    while sum(map(lambda x: high // x, times)) < n:
        high *= 2

    while low < high:
        middle = low + (high - low) // 2
        approved_num = sum(map(lambda x: middle // x, times))
        if approved_num >= n:
            high = middle
        if approved_num < n:
            low = middle + 1
    return low
