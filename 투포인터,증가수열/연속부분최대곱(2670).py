n = int(input())
a = []

for i in range(n):
    a.append(float(input()))

for i in range(1, n):
    a[i] = max(a[i], a[i - 1] * a[i])

print("%0.3f" % max(a))
