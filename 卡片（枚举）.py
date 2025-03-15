count = [2021] * 10  # 每个数字卡片2021张
a = 1  # 从1开始

while True:
    num_str = str(a)  # 将数字转换为字符串，方便逐位判断
    temp_count = count[:]  # 创建一个计数的临时副本，避免影响原始数据

    valid = True  # 标志位，判断是否可以拼出当前数字
    for digit in num_str:
        d = int(digit)
        if temp_count[d] > 0:
            temp_count[d] -= 1
        else:
            valid = False
            break

    if not valid:  # 如果无法拼出该数字，退出循环
        break

    count = temp_count  # 更新原始计数
    a += 1  # 尝试下一个数字

print(a - 1)  # 输出最后成功拼出的最大数字
