def max_square_side(two_by_two, one_by_one):
    max_units = two_by_two * 4 + one_by_one  # 计算最多的 1x1 小块数
    side = 0

    while (side + 1) ** 2 <= max_units:  # 逐步尝试最大的边长
        side += 1

    return side


# 已知的方块数量
two_by_two_blocks = 7385137888721
one_by_one_blocks = 10470245

# 计算最大正方形边长
result = max_square_side(two_by_two_blocks, one_by_one_blocks)
print(result-1)
