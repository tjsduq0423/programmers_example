def solution(citations):
    answer = len(citations)
    citations.sort()
    for i in citations:
        if i >= answer:
            return answer
        else:
            answer -= 1
    return answer


"""
어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

정렬한다 -> 
answer 보다 큰게 나온다면 그 이후는 전부 answer 보다 크다 ,
length  - 값에서 하나씩 줄인다 = > h번을 찾아간다 .

"""
