def solution(N, number):
    set_list = []
    
    for cnt in range(1, 9): # N의 갯수 1개부터 8개까지
        temp_set = set()
        temp_set.add(int(str(N) * cnt)) # N, NN, NNN... 의 경우 추가

        #set_list[i] => i+1 개의 N이 만들 수 있는 숫자 ex)set_list[0] => set(N)
        #점화식 정리 :N이 cnt 개일때 가능한 숫자는 (cnt-1,1),(cnt-2,2),(cnt-3,3)...(1,cnt-1)에서의 사칙연산값 전부
        for i in range(cnt - 1):
            for a in set_list[i]:
                for b in set_list[cnt - i - 2]:
                    temp_set.add(a + b)
                    temp_set.add(a * b)
                    temp_set.add(a - b)
                    if b != 0:
                        temp_set.add(a // b)
        
        # 가능한 숫자 집합에 number가 있는지 확인
        if number in temp_set:
            return cnt
        
        # 집합 추가
        set_list.append(temp_set)
    return -1
