"""
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.

"""

def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for idx, p in enumerate(prices): # 스택에 더 큰 값은 계속 채운다 .
        if not stack or stack[-1][1] <= p:
            stack.append((idx, p))
        else:
            while stack and stack[-1][1] > p: #  작은 값을 만나면 작은 값보다 큰 값들을 전부 뽑아서 지난 시간 idx 차이를 기록한다
                temp = stack.pop()
                answer[temp[0]] = idx - temp[0]
            stack.append((idx, p))
            
    while stack: # 주식시장이 끝나고 스택을 비우면서 마저 기록한다.
        temp = stack.pop()
        answer[temp[0]] = len(prices) - temp[0] - 1

    return answer

            