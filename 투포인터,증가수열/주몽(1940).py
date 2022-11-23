n = int(input())
m = int(input())
a = list(map(int, input().split()))

a.sort()
s, e = 0, n - 1
answer = 0

while s != e:
    temp = a[s] + a[e]
    if temp == m:
        answer += 1
        s += 1
    if temp < m:
        s += 1
    if temp > m:
        e -= 1

print(answer)
