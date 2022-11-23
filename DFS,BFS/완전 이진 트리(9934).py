k = int(input())
nodes = [int(i) for i in input().split(" ")]
answer = [[] for _ in range(k)]


def inorder(nodes, depth):
    if depth == k:
        return
    mid = len(nodes) // 2
    answer[depth].append(nodes[mid])
    inorder(nodes[:mid], depth + 1)
    inorder(nodes[mid + 1 :], depth + 1)


inorder(nodes, 0)

for i in answer:
    print(*i)
