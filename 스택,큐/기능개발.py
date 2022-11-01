def solution(progresses, speeds):
    answer = []
    progresses, speeds = progresses[::-1], speeds[::-1]
    while progresses:
        count = 0
        progresses = [p + s for p, s in zip(progresses, speeds)]
        while progresses and progresses[-1] >= 100:
            progresses.pop()
            speeds.pop()
            count += 1
        if count != 0:
            answer.append(count)
    return answer
