def solution(arr):
    result = [-1]
    for i in arr:
        if i != result[-1]:
            result.append(i)
    return result[1:]
    

print(solution([1,1,3,3,0,1,1]))