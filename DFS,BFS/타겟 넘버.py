def solution(numbers, target):
    x = [0] #  스택 업데이틀를 위한 list
    for i in numbers:
        y =[] # 더한 결과들을 저장해나갈 스택
        for j in x:
            y.append(j+i) 
            y.append(j-i)
        # 더하기 빼기 결과를 스택에 저장
        x = y
    # 모든 숫자를 전부 더하기 빼기한 결과가 x 에 저장됨.
    return x.count(target) # 모든 분기의 덧셈의 결과중 target 에 도달한 분기의 갯수 -> 타겟넘버를 만드는 방법의 수.
