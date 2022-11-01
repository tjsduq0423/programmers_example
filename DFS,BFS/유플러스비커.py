from collections import deque


def solution(sizes, target):
    answer = [[0, 0, 0]]
    queue = deque([([0, 0, 0], 0)])

    while queue:
        state, cnt = queue.popleft()

        if target in state:
            return cnt

        for s in range(4):  # 0123
            for e in range(4):  # 0123
                state_copy = [i for i in state]
                if s == e:  # 1 to 1 2 to 2 3 to 3 배제
                    continue
                if s == 3:  #  탱크 to e 번 비커 가득 채우기
                    state_copy[e] = sizes[e]
                    if state_copy not in answer:
                        answer.append(state_copy)
                        queue.append((state_copy, cnt + 1))
                    continue
                if e == 3:  # 비커 to 탱크 -> 물버리기
                    state_copy[s] = 0
                    if state_copy not in answer:
                        answer.append(state_copy)
                        queue.append((state_copy, cnt + 1))
                    continue
                if (
                    state_copy[s] != 0 and state_copy[e] != sizes[e]
                ):  # 물을 받는 비커가 가득차 있지 않을 때
                    water = min(
                        sizes[e] - state_copy[e], state_copy[s]
                    )  # 물을 따를 비커의 양과 따를 수있는 양중 적은 량을 이동
                    state_copy[e] += water
                    state_copy[s] -= water
                    if state_copy not in answer:
                        answer.append(state_copy)
                        queue.append((state_copy, cnt + 1))
        print(queue)

    return -1


"""

상태 , 진행 가능한 모든 방향

sizes  3, 5, 7 
target 1
가능한 경로
 0 1 2 3
1.  1번 비커를 가득 채운다
2.  2번 비커를 가득 채운다
3.  3번 비커를 가득 채운다
4.  1번 비커의 물을 2번에 가득 채운다
5.  1번 비커의 물을 3번에 가득
6.  2번 비커의 물을 1번에
7.  2번 비커의 물은 3번에
8.  3번 비커의 물을 1번에
9.  3번 비커의 물을 2번에 가득 채운다
10. 1번 비커의 물을 전부 버린다
11. 2번 비커의 물을 전부 버린다
12. 3번 비커의 물을 전부 버린다.


"""
