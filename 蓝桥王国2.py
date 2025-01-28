import heapq

def kth_shortest_path(n, m, edges_data, s, t, k):
    graph = {}
    for u, v, w in edges_data:
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))

    queue = [(0, s, 0)]  # 起点路径长度为 0，访问计数为 0
    heapq.heapify(queue)  # 将队列初始化为最小堆

    counts = {}

    while queue:
        cur_dist, node, count = heapq.heappop(queue)

        if node == t:
            count += 1
            if count == k:
                return cur_dist

        if node not in counts:
            counts[node] = 0
        counts[node] += 1

        # 如果当前节点的访问计数已经超过 k，跳过
        if counts[node] > k:
            continue

        if node in graph:
            for neighbor, weight in graph[node]:
                heapq.heappush(queue, (cur_dist + weight, neighbor, count))

    return -1

# 用户输入数据
lines = []
n, m = map(int, input().split())  # 读取节点数和边数
for _ in range(m):
    u, v, w = map(int, input().split())  # 读取每条边
    lines.append((u, v, w))

s, t, k = map(int, input().split())  # 读取起点、终点和第 k 短路径编号

# 调用函数并输出结果
result = kth_shortest_path(n, m, lines, s, t, k)
print(result)
