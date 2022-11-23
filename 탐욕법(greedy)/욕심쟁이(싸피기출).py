def greed(array, idx):  # True: 욕심쟁이 생존 후 보석 전부 처리 False: 욕심쟁이 폭발, idx 시작위치
    d = [i for i, ele in enumerate(array) if ele == "1"]

    while d:
        num = 10000
        temp = 0
        for j in d:
            if num == abs(j - idx):
                return False
            if num > abs(j - idx):
                temp = j
                num = abs(j - idx)
        idx = temp
        d.remove(idx)
    return True


tc = int(input())

for i in range(tc):
    n, m = map(int, input().split())
    arr = input().split(" ")
    answer = 0
    while True:
        if m - 1 - answer < 0 and m - 1 + answer >= len(arr):
            break
        if m - 1 - answer >= 0 and greed(arr, m - 1 - answer):
            break
        if m - 1 + answer < len(arr) and greed(arr, m - 1 + answer):
            break
        answer += 1

    print("#{} {}".format(i + 1, answer))
