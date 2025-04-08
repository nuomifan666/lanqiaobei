n = int(input())
li = list(map(int, input().split()))
s = 0

def is_poetic(x):
    if x < 3:
        return True
    if x % 2 == 1:  # 如果是奇数，说明是诗意数字，不删
        return False
    return is_poetic(x // 2)  # 一直除2直到小于3或为奇数

for i in range(n):
    if is_poetic(li[i]):
        s += 1

print(s)
