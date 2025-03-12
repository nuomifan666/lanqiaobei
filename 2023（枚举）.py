ans = 0
def find_i(i):
#具体来说，它查找第一个'2'的位置，然后从该位置的下一个字符开始查找'0'的位置......
    find_1 = i.find('2')
    if find_1 == -1:
        return 0

    find_2 = i.find('0', find_1 + 1)
    if find_2 == -1:
        return 0

    find_3 = i.find('2', find_2 + 1)
    if find_3 == -1:
        return 0

    find_4 = i.find('3', find_3 + 1)
    if find_4 == -1:
        return 0
    return 1

for i in range(12345678, 98765432 + 1):
    if find_i(str(i)) == 0:
        ans += 1
print(ans)


# def contains_2023(n):
#     s = str(n)
#     n = len(s)
#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 for l in range(k + 1, n):
#                     if s[i] == '2' and s[j] == '0' and s[k] == '2' and s[l] == '3':
#                         return True
#     return False
#
# def solve():
#     count = 0
#     for i in range(12345678, 98765433):  # 包含 98765432
#         if not contains_2023(i):
#             count += 1
#     return count
#
# result = solve()
# print(result)






