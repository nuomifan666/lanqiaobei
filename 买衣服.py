def main():
    import sys
    from collections import defaultdict
    import heapq

    n = int(input().strip())  # 读取 n
    prices = list(map(int, input().strip().split()))  # 读取价格列表
    a_colors = list(map(int, input().strip().split()))  # 读取第一种颜色
    b_colors = list(map(int, input().strip().split()))  # 读取第二种颜色
    m = int(input().strip())  # 读取 m
    customer_colors = list(map(int, input().strip().split()))  # 读取顾客颜色列表

    # T-shirt 数据
    tshirts = []
    for i in range(n):
        tshirts.append((prices[i], a_colors[i], b_colors[i]))

    # 每种颜色的最小堆
    color_to_heap = defaultdict(list)

    # 填充堆
    for price, a, b in tshirts:
        heapq.heappush(color_to_heap[a], price)
        heapq.heappush(color_to_heap[b], price)

    results = []

    # 处理每个顾客
    for color in customer_colors:
        if color in color_to_heap and color_to_heap[color]:
            min_price = heapq.heappop(color_to_heap[color])
            results.append(min_price)
        else:
            results.append(-1)

    # 输出结果
    print(" ".join(map(str, results)))


if __name__ == "__main__":
    main()
