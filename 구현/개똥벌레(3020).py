import sys

input = sys.stdin.readline

n, h = map(int, input().split(" "))

prefix_sum = [0] * h


for i in range(n):
    length = int(input())

    if i % 2 == 0:
        prefix_sum[h - length] += 1
    else:
        prefix_sum[0] += 1
        prefix_sum[length] -= 1

for i in range(1, h):
    prefix_sum[i] += prefix_sum[i - 1]

min_num = min(prefix_sum)
min_cnt = prefix_sum.count(min_num)

print(min_num, min_cnt)
