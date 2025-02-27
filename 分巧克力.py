# 读取输入
N, K = map(int, input().split())
chocolates = [tuple(map(int, input().split())) for _ in range(N)]

# 检查边长 S 是否可行
def can_cut(S):
    total = sum((H // S) * (W // S) for H, W in chocolates)
    return total >= K

# 二分搜索最大边长
left, right = 1, 100000
while left <= right:
    mid = (left + right) // 2
    if can_cut(mid):
        left = mid + 1  # 尝试更大的边长
    else:
        right = mid - 1  # 边长太大，减小
print(right)