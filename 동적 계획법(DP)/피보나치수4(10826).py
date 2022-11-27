# n = int(input())
#
# dp = [0] * (n + 1)
# dp[1] = 1
# for i in range(2, n + 1):
#     dp[i] = dp[i - 1] + dp[i - 2]
#
# print(dp[n])

n = int(input())

x = 0
y = 1
for i in range(n):
    x, y = y, x + y

print(x)
