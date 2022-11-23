n = int(input())
l = input().split()
min_num, max_num = str(10**10), "0"


def dfs(numbers, res, l_idx):
    global min_num, max_num
    if len(res) == n + 1:
        min_num = min_num if int(min_num) < int(res) else res
        max_num = max_num if int(max_num) > int(res) else res
        return

    for i in range(len(numbers)):
        if l[l_idx] == "<" and int(res[-1]) < numbers[i]:
            dfs(numbers[:i] + numbers[i + 1 :], res + str(numbers[i]), l_idx + 1)
        if l[l_idx] == ">" and int(res[-1]) > numbers[i]:
            dfs(numbers[:i] + numbers[i + 1 :], res + str(numbers[i]), l_idx + 1)
    return


zero_to_nine = list(range(10))
for i in range(10):
    dfs(zero_to_nine[:i] + zero_to_nine[i + 1 :], str(i), 0)

print(max_num)
print(min_num)


"""
k = int(input())
arr = input().split()

max_li = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
min_li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def check(n, input_list):
    if n < 0:
        return
    if arr[n] == '<' and input_list[n] < input_list[n + 1]:
        return
    if arr[n] == '>' and input_list[n] > input_list[n + 1]:
        return

    input_list[n], input_list[n + 1] = input_list[n + 1], input_list[n]

    check(n - 1, input_list)


for i in range(k):
    check(i, max_li)
    check(i, min_li)

print(*max_li[:k + 1],sep='')
print(*min_li[:k + 1],sep='')
"""

"""
def good(x, y, op) :
  if op == '<' :
    if x > y : return False
  if op == '>' :
    if x < y : return False
  return True

def go(index, num) :
  if index == n+1 : # 부등호가 n개 입력되니까 숫자는 n+1개 필요
    ans.append(num)
    return
  
  for i in range(10) :
    if check[i]: continue # 해당 숫자를 이미 사용했다면 pass

    if index == 0 or good(num[index-1], str(i), a[index-1]):
      check[i] = True
      go(index+1, num+str(i))
      check[i] = False

n = int(input())
a = input().split()

ans = []
check = [False]*10 # 해당 숫자를 사용했는지 안 했는지 체크

go(0, '')

ans.sort()
print(ans[-1])
print(ans[0])

"""
