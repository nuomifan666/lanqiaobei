def find_position(N): 
    position = 0  # 记录当前序列中的位置（从 1 开始计数）
    n = 0  # 记录当前处理的行数
    
    while True:  # 无限循环，直到找到 N
        position += 1  # 每进入新行时，先把首个 '1' 计入序列
        if 1 == N:  # 如果 N 是 1，直接返回位置
            return position

        current = 1  # 当前杨辉三角的数值，首个 always 是 1
        for k in range(1, n + 1):  # 计算这一行的所有值（除了第一个 1）
            current = current * (n - k + 1) // k  # 计算组合数 C(n, k)
            position += 1  # 当前位置增加
            if current == N:  # 找到 N，返回位置
                return position
                
        n += 1  # 进入下一行

N = int(input())  # 读取输入
print(find_position(N))  # 输出 N 在杨辉三角序列中的首次出现位置
