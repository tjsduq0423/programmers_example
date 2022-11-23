h, w = map(int, input().split())
b_h = list(map(int, input().split()))

answer = 0
for i in range(1, w - 1):
    a = min(max(b_h[:i]), max(b_h[i + 1 :]))
    if b_h[i] < a:
        answer += a - b_h[i]

print(answer)
