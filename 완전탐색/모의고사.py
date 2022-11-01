def solution(answers):
    marking_way = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]
    count_arr = []

    for way in marking_way:
        way = way * 2000
        count = 0

        for w, a in zip(way[: len(answers)], answers):
            if a == w:
                count += 1

        count_arr.append(count)

    m = max(count_arr)

    answer = []

    for idx, cnt in enumerate(count_arr):
        if m == cnt:
            answer.append(idx + 1)

    return answer


"""

def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

"""
