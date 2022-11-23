# t = int(input())

# for _ in range(t):
#     n, m = map(int, input().split())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     d = [0] * n
#     a.sort()
#     b.sort()

#     for i in range(n):
#         temp = 0
#         for j in range(d[i - 1], m):
#             if a[i] > b[j]:
#                 temp += 1
#         d[i] = temp + d[i - 1]
#     print(sum(d))


for _ in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    count = 0
    pair = 0

    for i in range(N):
        while True:
            if count == M or A[i] <= B[count]:
                pair += count
                break
            else:
                count += 1

    print(pair)
