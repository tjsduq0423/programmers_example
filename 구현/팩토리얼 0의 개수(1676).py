n = int(input())

two = 0
five = 0
for i in range(1, n + 1):
    temp = i
    while temp % 2 == 0 or temp % 5 == 0:
        if temp % 2 == 0:
            temp = temp // 2
            two += 1
        if temp % 5 == 0:
            temp = temp // 5
            five += 1
print(min(two, five))
