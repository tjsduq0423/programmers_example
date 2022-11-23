n, l = map(int, input().split())
a = []

for i in range(n):
    a.append(tuple(map(int, input().split())))

a.sort()

right = 0
answer = 0

for i, j in a:
    if right < i:
        right = i
    while right < j:
        answer += 1
        right += l
print(answer)
