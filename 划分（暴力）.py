def max_partition_product(nums):
    n = len(nums)
    total_sum = sum(nums)
    max_product = 0

    # 遍历所有可能的划分（从 1 到 2^n - 2，确保每组至少有一个元素）
    for mask in range(1, 1 << n):
        group1_sum = sum(nums[i] for i in range(n) if mask & (1 << i))
        group2_sum = total_sum - group1_sum
        product = group1_sum * group2_sum
        max_product = max(max_product, product)

    return max_product

# 给定的 40 个数
numbers = [
    5160, 9191, 6410, 4657, 7492, 1531, 8854, 1253, 4520, 9231,
    1266, 4801, 3484, 4323, 5070, 1789, 2744, 5959, 9426, 4433,
    4404, 5291, 2470, 8533, 7608, 2935, 8922, 5273, 8364, 8819,
    7374, 8077, 5336, 8495, 5602, 6553, 3548, 5267, 9150, 3309
]

# 计算最大划分权值
result = max_partition_product(numbers)
print("最大划分权值为:", result)
