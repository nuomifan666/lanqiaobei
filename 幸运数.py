count = 0
for digits in range(2, 9, 2):  # 只考虑偶数位数的数字
    start = 10 ** (digits - 1)
    end = 10 ** digits
    for i in range(start, end):
        str_i = str(i)
        if sum(int(str_i[j]) for j in range(len(str_i) // 2)) == sum(int(str_i[j]) for j in range(len(str_i) // 2, len(str_i))):
            count += 1

print(count)







#错误示范
# count=0
# for i in range(10,100000000,1):
#   str_i=str(i)
#   if len(str_i)%2==0:
#     res1=sum(int(a) for a in range(len(str_i)//2))
#     res2=sum(int(b) for b in range(len(str_i)//2,len(str_i)))
#     if res1 == res2:
#       count+=1
# print(count)












# count = 0
# for num in range(1, 100000000):
#     str_num = str(num)
#     if len(str_num) % 2 == 0:
#         num_center = len(str_num) // 2
#         if sum(map(int, str_num[:num_center])) == sum(map(int, str_num[num_center:])):
#             count += 1
#
# print(count)
#
# count = 0
#
# for num in range(1, 100000000):
#     str_num = str(num)
#     if len(str_num) % 2 == 0:  # 只检查偶数位数的数字
#         num_center = len(str_num) // 2
#         left_sum = 0
#         right_sum = 0
#
#         for i in range(num_center):  # 计算左半部分的数位和
#             left_sum += int(str_num[i])
#
#         for i in range(num_center, len(str_num)):  # 计算右半部分的数位和
#             right_sum += int(str_num[i])
#
#         if left_sum == right_sum:
#             count += 1

# print(count)

# count=0
# for num in range(1,100000000):
#     str_num=str(num)
#     if len(str_num)%2==0:
#         num_center=len(str_num)//2
#         if sum(str_num[:num_center])==sum(str_num[num_center+1:]):
#             count+=1
#
# print(count)