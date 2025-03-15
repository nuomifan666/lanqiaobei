count = 0
for num in range(1, 100000000):
    str_num = str(num)
    if len(str_num) % 2 == 0:
        num_center = len(str_num) // 2
        if sum(map(int, str_num[:num_center])) == sum(map(int, str_num[num_center:])):
            count += 1

print(count)

count = 0

for num in range(1, 100000000):
    str_num = str(num)
    if len(str_num) % 2 == 0:  # 只检查偶数位数的数字
        num_center = len(str_num) // 2
        left_sum = 0
        right_sum = 0

        for i in range(num_center):  # 计算左半部分的数位和
            left_sum += int(str_num[i])

        for i in range(num_center, len(str_num)):  # 计算右半部分的数位和
            right_sum += int(str_num[i])

        if left_sum == right_sum:
            count += 1

print(count)

# count=0
# for num in range(1,100000000):
#     str_num=str(num)
#     if len(str_num)%2==0:
#         num_center=len(str_num)//2
#         if sum(str_num[:num_center])==sum(str_num[num_center+1:]):
#             count+=1
#
# print(count)