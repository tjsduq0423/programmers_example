from itertools import permutations


def solution(name):
    if set(name) == {"A"}:
        return 0

    default_name = ["A"] * len(name)
    num = [
        min(ord(n) - ord(d), 26 - (ord(n) - ord(d)))
        for n, d in zip(list(name), default_name)
    ]  # 상하 이동 전부 계산

    destinations = [
        i for i in range(len(name)) if name[i] != "A" and i != 0
    ]  # 좌우 이동으로 거쳐야하는 알파벳 index

    all_cases = permutations(destinations, len(destinations))  # 이동시 모든 경우의 수
    min_distance = 999999  # 모든 경우 중 가장 짤은 조작거리를 구해 넣을 변수

    for case in all_cases:
        now = 0  # 출발 index
        distance = 0

        for next in case:
            distance += min(
                abs(next - now), len(name) - abs(next - now)
            )  # 좌 or우방향 거리 중 짧은 거리
            now = next  # 경로 순회
            if distance > min_distance:  # 가장 짧은 조작수를 넘어가면 연산 종료
                break

        min_distance = min(min_distance, distance)

    return sum(num) + min_distance  # 상하조작 수 + 좌우 조작 수


print(solution("FJLQKENLFFNS"))
