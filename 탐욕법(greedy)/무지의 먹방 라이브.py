def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    times = k
    e_food_times = list(enumerate(food_times))
    e_food_times.sort(key=lambda x: x[1], reverse=True)  # idx, value 후에 value로 내림차순 정렬

    while times // len(e_food_times):  #
        cycle_count = min(e_food_times[-1][1], times // len(e_food_times))
        times -= cycle_count * len(e_food_times)
        e_food_times = [
            (idx, ele - cycle_count)
            for (idx, ele) in e_food_times
            if ele - cycle_count != 0
        ]

    e_food_times.sort(key=lambda x: x[0])  # 남은 times로는 food_times의 한 사이클을 순회 할 수 없는 상황
    # times에 남겨진 값들 중 times + 1 번째의 index  부터 다시 먹으면 된다.
    return e_food_times[times][0] + 1
