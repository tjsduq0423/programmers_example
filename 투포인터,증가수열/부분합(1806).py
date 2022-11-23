n, s = map(int, input().split())
a = list(map(int, input().split()))

start, end = 0, 0
sub_s = a[0]
ans = 100000

while True:
    if sub_s >= s:
        sub_s -= a[start]
        ans = min(ans, end - start + 1)
        start += 1
    else:
        end += 1
        if end == n:
            break
        sub_s += a[end]

ans = 0 if ans == 100000 else ans
print(ans)
