# DFS로 풀이
def solution(numbers, target, idx=0, sumation=0):
    # 모든 숫자를 연산했다면 target에 도달했는지 확인하고 리턴
    if len(numbers) == idx:
        return 1 if target == sumation else 0
    # 연산 중이라면 현재 index 에서 연산
    else:
        return solution(numbers, target, idx + 1, sumation + numbers[idx]) + solution(
            numbers, target, idx + 1, sumation - numbers[idx]
        )


# 다른 사람의 풀이
def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target - numbers[0]) + solution(
            numbers[1:], target + numbers[0]
        )
