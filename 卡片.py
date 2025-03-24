count = [2021] * 10  # 每个数字卡片有 2021 张
num = 1

while True:
    str_num = str(num)  # 将当前数字转成字符串
    for i in str_num:
        anum = int(i)
        if count[anum] == 0:
            print(num-1)  # 输出当前不能拼出的数
            exit()  # 直接结束程序
    # 只有当 num 的所有数字都可以使用时，才减少对应卡片的数量
    for i in str_num:
        count[int(i)] -= 1
    num += 1  # 只有拼出一个完整的数字后才增加





# count=[2021]*10
# num=1
# while True:
#     str_num=str(num)
#     for i in str_num:
#         anum=int(i)
#         if count[anum]==0:
#             print(str_num)
#
#         else:
#             count[anum]-=1
#             num+=1


