from collections import deque


def solution(s):
    if s[0] == ")" or s[-1] == "(" or len(s) % 2:
        return False

    queue = deque(s)
    stack = []
    
    while queue:
        q = queue.popleft()

        if not stack:
            if q == ")":
                return False
            stack.append(q)
        else:
            if stack[-1] != q:
                stack.pop()
            stack.append(q)

    
    return True

    """
    def solution(s):
    answer=0
    if s.count('(')!=s.count(")"):
        return False


    for i in s:
        if i=='(':
            answer+=1
        else:
            answer-=1

        if answer<0:
            return False


    return True
    """