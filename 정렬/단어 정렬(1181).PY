n = int(input())
a = set()  # 중복 제거
for i in range(n):
    a.add(input())
res = list(a)
res.sort()  # 사전순 정렬
res.sort(key=len)  # 길이순 정렬
for i in res:
    print(i)
