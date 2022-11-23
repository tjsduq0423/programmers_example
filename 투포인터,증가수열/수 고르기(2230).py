N, M = map(int, input().split())
A = []

for i in range(N):
    A.append(int(input()))

A.sort()

start, end = 0, 0
ans = A[-1] - A[0]

while start < N and end < N:
    temp = A[end] - A[start]
    if temp >= M:
        ans = min(ans, temp)
        start += 1
    else:
        end += 1
print(ans)
