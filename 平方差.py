sum1 = 0
a = set()
for i in range(2022):
    for j in range(i, 2022):
        end = j ** 2 - i ** 2
        if end > 2022:
            break
        else:
            a.add(end)

print(len(a) - 1)  # 1-2021 所以0 不在范围内，要减去！！！















# count = 0
# unique_numbers = set()
#
# for i in range(1, 2022):
#     found = False  # 记录是否找到该 i 的解
#     for a in range(1, i):
#         for b in range(0, a):
#             if a**2 - b**2 == i:
#                 unique_numbers.add(i)
#                 found = True
#                 break  # 结束 b 循环
#         if found:
#             break  # 结束 a 循环
#
# print(len(unique_numbers))
#
# # count = 0
# # unique_numbers = set()  # 用于去重
# #
# # for i in range(1, 2022):
# #     for a in range(1, i):
# #         for b in range(0, a):  # b 可以是 0
# #             if a**2 - b**2 == i:
# #                 unique_numbers.add(i)  # 只记录数值，去重
# #                 break  # 找到一种表示方式就够了，防止重复计数
# #
# # print(len(unique_numbers))
#
#
#
#
#
#
#
#
#
#
# # count=0
# # for i in range(1,2022):
# #   for a in range(1,i):
# #     for b in range(1,a):
# #       if a**2-b**2==i:
# #         count+=1
# #         continue
# # print(count)