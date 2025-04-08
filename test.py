def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 分解：将列表分成两半
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # 递归排序左半部分
    right_half = merge_sort(arr[mid:])  # 递归排序右半部分

    # 合并：将两个有序子列表合并
    return merge(left_half, right_half)


def merge(left, right):
    sorted_arr = []
    i = j = 0

    # 比较两个子列表的元素，按顺序合并
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # 将剩余的元素添加到结果中
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr


# 示例
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # 输出: [3, 9, 10, 27, 38, 43, 82]