def cal(a, b):
    c = 0.08869
    return ((a * c + 100) / (b * c + 100)) * 100


print(cal(1771, 1750))
