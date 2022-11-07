import heapq as hq


def solution(scoville, K):
    answer = 0
    copy_scoville = [i for i in scoville]

    hq.heapify(copy_scoville)

    while copy_scoville[0] <= K and len(copy_scoville) > 1:
        hq.heappush(
            copy_scoville, hq.heappop(copy_scoville) + hq.heappop(copy_scoville) * 2
        )
        answer += 1

    return answer if copy_scoville[0] >= K else -1
