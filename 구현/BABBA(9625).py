# k = int(input())
# text = 'A'
#
# for i in range(k):
#     temp = ""
#     for c in text:
#         if c == 'A':
#             temp += 'B'
#         if c == 'B':
#             temp += 'BA'
#     text = temp
#
# print("{} {}".format(text.count('A'), text.count('B')))

k = int(input())
a = 1
b = 0

for i in range(k):
    a, b = b, b + a

print("%d %d" % (a, b))
