def count_unique_weights(N, weights):
    # 使用集合来存储不同的重量
    unique_weights = set()
    
    # 递归函数来计算所有可能的重量
    def calculate_weight(index, current_weight):
        if index == N:
            unique_weights.add(current_weight)
            return
        
        # 不使用当前砝码
        calculate_weight(index + 1, current_weight)
        
        # 将当前砝码放在左边
        calculate_weight(index + 1, current_weight + weights[index])
        
        # 将当前砝码放在右边
        calculate_weight(index + 1, current_weight - weights[index])
    
    # 从第0个砝码开始，初始重量为0
    calculate_weight(0, 0)
    
    # 返回不同重量的数量
    return len(unique_weights)

# 输入处理
N = int(input())
weights = list(map(int, input().split()))

# 计算并输出结果
result = count_unique_weights(N, weights)
print(result)
