import collections

graph = collections.defaultdict(list)


def compare(word_a, word_b):
    diff_num = 0

    for a, b in zip(word_a, word_b):
        if a != b:
            diff_num += 1

    if diff_num == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    words += [begin]
    while words:
        cmp_word = words.pop()
        for word in words:
            if compare(cmp_word, word):
                graph[cmp_word].append(word)
                graph[word].append(cmp_word)

    queue = collections.deque([(begin, 0)])
    visited = [begin]

    while queue:
        word, count = queue.popleft()

        for next in graph[word]:
            if next == target:
                return count + 1
            if next not in visited:
                visited.append(next)
                queue.append((next, count + 1))

    return 0
