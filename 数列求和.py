a, b, c = 1, 1, 1
for _ in range(4, 20190325):
    a, b, c = b%10000, c%10000, (a + b + c)%10000
print(c)





# a = [0] * 20190325  # 创建足够大的数组
# a[0], a[1], a[2], a[3], a[4] = 0, 1, 1, 1, 3
#
# for i in range(5, 20190325):  # 从索引 5 开始填充
#     a[i] = a[i - 1] + a[i - 2] + a[i - 3]
#
# print(a[20190324])  # 输出第 20190324 个数