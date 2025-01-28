# 读取迷宫的行数n和列数m
n, m = map(int, input().split())

# 使用列表推导式读取迷宫数据，逐行转换成整数并保存在gra二维数组中
# 每一行通过 input().split() 先转换成字符串列表，再用 map(int, ...) 转换为整数
gra = [list(map(int, input().split())) for i in range(n)]

# 定义四个方向的移动：下、上、右、左
dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

# 读取起点和终点的坐标，转换为从0开始的索引
x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1  # 转换为0-based坐标

# 初始化队列，保存起点坐标和步数
q = [[x1, y1, 0]]  # 队列中每个元素是一个列表： [x, y, dis]，其中dis是当前的步数

# 设置标志变量f，判断是否找到终点
f = True

# 广度优先搜索（BFS）循环
while q:
    # 从队列中取出第一个元素
    x, y, dis = q.pop(0)  # x, y 是当前的位置，dis 是到该位置的步数

    # 如果当前坐标等于终点坐标，输出步数并结束搜索
    if x == x2 and y == y2:
        f = False  # 找到终点，设置 f 为 False
        print(dis)  # 输出当前步数，即最短路径的步数
        break  # 退出循环，结束程序

    # 遍历四个方向
    for xx, yy in dirs:
        # 计算新位置的坐标
        tx, ty = xx + x, yy + y

        # 检查新位置是否合法（在迷宫范围内且是可走的地方，即 gra[tx][ty] == 1）
        if tx >= 0 and tx < n and ty >= 0 and ty < m and gra[tx][ty] == 1:
            gra[tx][ty] = 0  # 标记新位置为已访问，避免重复访问
            q.append([tx, ty, dis + 1])  # 将新位置加入队列，并更新步数

# 如果搜索结束后 f 仍然为 True，表示没有找到终点，输出 -1
if f:
    print(-1)

