def solution(word):
    count = []
    
    def dfs(w, word):
        count.append(0)
        if w == word:
            count.append(1)
            return True
        if len(w) == 5:
            return False
        for i in ["A", "E", "I", "O", "U"]:
            if dfs(w + i, word):
                return True
    
    if dfs("", word):
        print(count)
        return count.index(1) -1
