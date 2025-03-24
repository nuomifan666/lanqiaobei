n, k = map(int, input().split())
arr = []
shuchu = []  # 用于记录已经输出的最大值

# 读取数组元素
for _ in range(n):
    arr.append(int(input()))

# 处理滑动窗口
for i in range(n - k + 1):
    window = arr[i:i + k]
    max_window = max(window)

    # 如果最大值已经出现过，输出 "Nothing"
    if max_window in shuchu:
        print("Nothing")
    else:
        # 否则输出最大值，并记录已出现的最大值
        shuchu.append(max_window)
        print(max_window)

# n,k=map(int,input().split())
# arr=[]
# shuchu=set()
# for _ in range(n):
#     arr.append(int(input()))
# for i in range(n-k+1):
#     window=arr[i:i+k]
#     max_window=max(window)
#     if max_window in shuchu:
#         print("Nothing")
#     else:
#         shuchu.add(max_window)
# print("\n".join(shuchu))
# join只能用于字符串