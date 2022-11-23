n = int(input())
a = []
for i in range(n):
    a.append(tuple(map(int, input().split())))

a.sort()

left, right = a[0]
ans = 0

for i, j in a:
    if j <= right:
        continue
    if i > right:
        ans += right - left
        left, right = i, j
    if i <= right:
        right = j
ans += right - left

print(ans)
