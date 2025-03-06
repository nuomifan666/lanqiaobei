def max_reward(n, m, grid):
    # 初始化 dp 数组
    dp = [[-float('inf')] * m for _ in range(n)]
    dp[0][0] = grid[0][0]  # 起点的权值

    # 遍历每个格子
    for i in range(n):
        for j in range(m):
            # 如果当前格子不可达，则跳过
            if dp[i][j] == -float('inf'):
                continue
            
            # 计算可以到达的格子
            for di in range(4):  # 行差 0, 1, 2, 3
                for dj in range(4):  # 列差 0, 1, 2, 3
                    ni = i + di
                    nj = j + dj
                    if ni < n and nj < m:  # 确保在边界内
                        dp[ni][nj] = max(dp[ni][nj], dp[i][j] + grid[ni][nj])

    return dp[n-1][m-1]  # 返回右下角的最大权值和

# 输入处理
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 计算并输出结果
result = max_reward(n, m, grid)
print(result)

'''
import sys

def dfs(grid, x, y, n, m, current_sum):
    """深度优先搜索，暴力遍历所有路径"""
    if x == n - 1 and y == m - 1:  # 到达终点
        return current_sum + grid[x][y]

    max_value = -sys.maxsize  # 记录最大权值和
    for dx, dy in [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (3, 0)]:
        nx, ny = x + dx, y + dy
        if nx < n and ny < m:  # 确保不越界
            max_value = max(max_value, dfs(grid, nx, ny, n, m, current_sum + grid[x][y]))

    return max_value

def max_reward(grid, n, m):
    return dfs(grid, 0, 0, n, m, 0)
'''