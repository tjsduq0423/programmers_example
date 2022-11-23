n = int(input())
a = list(map(int, input().split()))
x = int(input())

a.sort()

s, e = 0, n - 1
ans = 0

while e != s:
    temp = a[s] + a[e]
    if temp > x:
        e -= 1
    if temp == x:
        ans += 1
        s += 1
    if temp < x:
        s += 1
print(ans)
