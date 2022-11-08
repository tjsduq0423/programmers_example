N = input()
length = len(N)
middle_idx = length // 2

sumation1 = sum(map(int, list(N[:middle_idx])))
sumation2 = sum(map(int, list(N[middle_idx:])))

if sumation1 == sumation2:
    print("LUCKY")
else:
    print("READY")
