nn = 4000001
n = int(input())

p = []
c = [True] * nn

for i in range(2, int(nn**0.5) + 1):
    if c[i]:
        for j in range(i + i, nn, i):
            c[j] = False

for i in range(2, n + 1):
    if c[i]:
        p.append(i)

cnt = 0
temp = 0
left, right = 0, 0
while True:
    if temp >= n:
        temp -= p[left]
        left += 1
    elif right == len(p):
        break
    else:
        temp += p[right]
        right += 1
    if temp == n:
        cnt += 1
print(cnt)

"""
첫번째, temp 값이 n보다 크거나 같으면 시작 포인트를 하나 올려준다. 시작 포인트 상승 ->  temp 값 감소

두번째, 끝 포인트가 len(p)에 도달했으면 break 해준다. 

세번째, temp 값이 n보다 작으면 끝 포인트를 증가시켜준다. 끝포인트 증가 > temp값증가 

네번째, temp 와 n 이 같으면 카운팅 해준다. 
"""
