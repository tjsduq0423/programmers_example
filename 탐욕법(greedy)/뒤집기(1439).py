S = input()

if len(S) != 0:
    temp = S[0]
    c_cnt = 0
else:
    print(0)

for num in S:
    if temp != num:
        c_cnt += 1
        temp = num

answer = c_cnt // 2 if c_cnt % 2 == 0 else c_cnt //2 + 1

print(answer)