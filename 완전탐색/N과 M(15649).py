# import itertools

# n, m = map(int, input().split())
# nums = [i for i in range(1, n + 1)]

# array = itertools.permutations(nums, m)

# for i in array:
#     print(*i)


n, m = map(int, input().split())
nums = [i for i in range(1, n + 1)]
answer = []


def dfs():
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return

    for i in range(1, n + 1):
        if i not in answer:
            answer.append(i)
            dfs()
            answer.pop()


dfs()
