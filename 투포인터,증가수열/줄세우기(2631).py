n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

# d[i] : a[i]를 마지막 값으로 가지는 가장 긴 증가부분수열의 길이
d = [1] * n

for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))
