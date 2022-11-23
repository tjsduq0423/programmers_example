from collections import deque


n = 10000
a = [True] * n

for i in range(2, int(n**0.5) + 1):
    if a[i]:
        for j in range(i + i, n, i):
            a[j] = False


def BFS(p1, p2):
    visited = [False] * 10000
    visited[int(p1)] = True
    queue = deque([p1])
    cnt = 0

    while queue:
        l = len(queue)
        while l > 0:
            q = queue.popleft()
            if q == p2:
                return cnt

            for i in range(4):
                for j in range(10):
                    next = int(q[:i] + str(j) + q[i + 1 :])
                    if 1000 <= next < 10000 and a[next] and not visited[next]:
                        queue.append(str(next))
                        visited[next] = True
            l -= 1
        cnt += 1
    return "Impossible"


test_case = int(input())

for i in range(test_case):
    p1, p2 = input().split()
    print(BFS(p1, p2))

"""
# make the sieve of Eratosthenes.
primes = set(range(2, 10000))
for i in range(2, 101):
    if i in primes:
        primes -= set(range(i * i, 10000, i))
primes -= set(range(2, 1000))
primes = set(map(str, primes))  # consider the passwords as string.


def solution() -> int:
    src, dest = input().split()
    queue = collections.deque([(src, 0)])
    visits = set()

    while queue:
        password, level = queue.popleft()
        digits = list(password)

        if password not in primes or password in visits:
            continue
        visits.add(password)
        if password == dest:
            return level  # possible

        for i in range(4):
            temp = digits[i]
            for num in range(10):
                digits[i] = str(num)
                queue.append(("".join(digits), level + 1))
            digits[i] = temp

    return -1  # impossible


# main
for _ in range(int(input())):
    result = solution()
    print("impossible" if result == -1 else result)


"""
