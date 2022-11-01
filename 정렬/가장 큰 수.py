def solution(numbers):
    if sum(numbers) == 0:
        return "0"
    numbers = list(map(str, numbers))
    N = [(num, (num * 10)[:10]) for num in numbers]
    sorted_N = sorted(N, key=lambda x: x[1], reverse=True)

    return "".join([n[0] for n in sorted_N])

    """
    23 -> 2323232323 으로 만들어서 이걸 기준으로 정렬

    
    """
