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

