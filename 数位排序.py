def digit_sum(num):
    """计算一个数的数位之和"""
    return sum(int(digit) for digit in str(num))


def find_mth_element(n, m):
    """找到排序后的第m个元素"""
    # 生成1到n的列表
    numbers = list(range(1, n + 1))

    # 按照数位之和和数值大小进行排序
    sorted_numbers = sorted(numbers,key=lambda x:(digit_sum(x),x))

    # 返回第m个元素（注意Python的索引从0开始，所以要减1）
    return sorted_numbers[m - 1]


# 输入
n = int(input())
m = int(input())

# 输出结果
print(find_mth_element(n, m))
