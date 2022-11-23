from collections import deque

n = int(input())
m = int(input())
d = abs(n - 100)

if m == 0:
    print(min(d, len(str(n))))
    exit(0)

a = list(map(int, input().split()))
b = [str(i) for i in range(10) if i not in a]

queue = deque([("")])

while queue:
    q = queue.popleft()
    print(q)
    temp = abs(n - int(q)) if q else n
    d = min(d, temp + n)
    for i in b:
        if temp > abs(n - int(q + i)):
            queue.append(q + i)

print(d)
