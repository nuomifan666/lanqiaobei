# 读取三行输入，并去除每行的前后空格
lines = [input().strip() for _ in range(3)]

# 统计每行的元音数目
counts = []
for line in lines:
    count = 0
    for char in line:
        if char in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    counts.append(count)

# 检查是否符合5-7-5的结构
if counts == [5, 7, 5]:
    print("YES")
else:
    print("NO")
