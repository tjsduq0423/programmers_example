n, m = map(int, input().split())

sl = list(map(int, input().split()))

ans = 0
start, end = 0, 0
while start <= n and end <= n:
    temp = sum(sl[start : end + 1])
    if temp == m:
        ans += 1
        start += 1
    if temp < m:
        end += 1
    if temp > m:
        start += 1

print(ans)
