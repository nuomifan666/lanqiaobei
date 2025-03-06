import heapq
import math

# 计算 LCM（最小公倍数）
def lcm(a, b):
    return a * b // math.gcd(a, b)

# Dijkstra 算法
def dijkstra():
    INF = float('inf')
    dist = [INF] * 2022  # 记录从1到各个点的最短路径
    dist[1] = 0  # 起点到自身距离为0
    pq = [(0, 1)]  # (当前距离, 节点编号) 优先队列
    
    while pq:
        d, node = heapq.heappop(pq)  # 取出当前最短路径的点
        if d > dist[node]:  # 如果当前距离比已知最短路径长，跳过
            continue
        
        # 遍历相邻的点 (node+1 到 node+21)
        for next_node in range(node + 1, min(node + 22, 2022)):
            cost = lcm(node, next_node)  # 计算最小公倍数作为边的权重
            if dist[next_node] > dist[node] + cost:  # 更新最短路径
                dist[next_node] = dist[node] + cost
                heapq.heappush(pq, (dist[next_node], next_node))
    
    return dist[2021]  # 返回到 2021 号点的最短路径

# 输出答案
print(dijkstra())
