# n = int(input())
# numbers = list(map(int, input().split()))
# operator_nums = list(map(int, input().split()))
# l = len(numbers)
# answer = []


# def dfs(oper, cnt, res):
#     global answer
#     if cnt == l - 1:
#         answer += [res]
#         return
#     for i in range(4):
#         if oper[i] == 0:
#             continue
#         if i == 0:
#             oper[i] -= 1
#             dfs(oper, cnt + 1, res + numbers[cnt + 1])
#             oper[i] += 1
#         if i == 1:
#             oper[i] -= 1
#             dfs(oper, cnt + 1, res - numbers[cnt + 1])
#             oper[i] += 1
#         if i == 2:
#             oper[i] -= 1
#             dfs(oper, cnt + 1, res * numbers[cnt + 1])
#             oper[i] += 1
#         if i == 3:
#             oper[i] -= 1
#             dfs(
#                 oper,
#                 cnt + 1,
#                 -(abs(res) // numbers[cnt + 1]) if res < 0 else res // numbers[cnt + 1],
#             )
#             oper[i] += 1
#     return
# dfs(operator_nums, 0, numbers[0])
# print(max(answer))
# print(min(answer))

n = int(input())
numbers = list(map(int, input().split()))
operator_nums = list(map(int, input().split()))
max_num = 0
min_num = 100000


def dfs(plus, minus, mul, divi, res, cnt):
    global max_num, min_num
    if plus < 0 or minus < 0 or mul < 0 or divi < 0:
        return
    if cnt == n:
        max_num = max(max_num, res)
        min_num = min(min_num, res)
        return

    next = res + numbers[cnt]
    dfs(plus - 1, minus, mul, divi, next, cnt + 1)
    next = res - numbers[cnt]
    dfs(plus, minus - 1, mul, divi, next, cnt + 1)
    next = res * numbers[cnt]
    dfs(plus, minus, mul - 1, divi, next, cnt + 1)
    next = res // numbers[cnt] if res > 0 else -((-res) // numbers[cnt])
    dfs(plus, minus, mul, divi - 1, next, cnt + 1)


dfs(*operator_nums, numbers[0], 1)
print(max_num)
print(min_num)
