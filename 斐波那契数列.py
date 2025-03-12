def count_fibonacci_with_last_digit_seven(n):
    if n < 1:
        return 0

    # 初始化前两个斐波那契数
    f1, f2 = 1, 1
    count = 0

    # 统计个位数为7的斐波那契数
    for _ in range(1, n + 1):
        if f1 % 10 == 7:
            count += 1
        f1, f2 = f2, (f1 + f2) % 10  # 只保留个位数

    return count


# 计算前202202011200项中个位为7的数量
n = 202202011200
result = count_fibonacci_with_last_digit_seven(n)
print(result)
