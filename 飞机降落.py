def can_land_all_planes(current_plane, current_time):
    """
    递归检查是否可以安全降落所有飞机。

    :param current_plane: 当前尝试降落的飞机编号（从0开始）
    :param current_time:  当前跑道可用时间
    """
    global is_possible

    if current_plane == total_planes:
        # 如果所有飞机都降落了，则成功
        is_possible = True
        return

    if is_possible:
        # 如果已经找到可行解，则提前返回
        return

    for i in range(total_planes):
        if has_landed[i] == 0:  # 当前飞机未降落
            earliest_landing_time = arrival_times[i]  # 该飞机最早降落时间
            latest_landing_time = arrival_times[i] + max_hover_times[i]  # 该飞机最晚降落时间

            if latest_landing_time < current_time:
                # 如果飞机无法在当前时间降落，则方案失败
                is_possible = False
                return

            # 标记飞机为已降落
            has_landed[i] = 1
            # 计算下一架飞机降落时刻，必须是当前飞机的降落时间和跑道空闲时间的最大值
            next_time = max(current_time, earliest_landing_time) + landing_durations[i]
            can_land_all_planes(current_plane + 1, next_time)
            # 回溯：取消飞机降落标记
            has_landed[i] = 0


# 读取测试数据组数
T = int(input())

for _ in range(T):
    # 读取飞机数量
    total_planes = int(input())
    arrival_times = [0] * total_planes  # 飞机到达时间
    max_hover_times = [0] * total_planes  # 飞机最大盘旋时间
    landing_durations = [0] * total_planes  # 飞机降落所需时间

    for j in range(total_planes):
        arrival_times[j], max_hover_times[j], landing_durations[j] = map(int, input().split())

    is_possible = False  # 记录是否所有飞机可以安全降落
    has_landed = [0] * total_planes  # 记录飞机是否已降落

    # 尝试从第 0 架飞机开始降落
    can_land_all_planes(0, 0)

    print("YES" if is_possible else "NO")
