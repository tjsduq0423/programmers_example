check = [True] * 10001
for i in range(1, 10001):
    if check[i]:
        s_num = i
        while s_num < 10001:
            s_num += sum(map(int, str(s_num)))
            if s_num < 10001:
                check[s_num] = False

for i in range(1, 10001):
    if check[i]:
        print(i)
