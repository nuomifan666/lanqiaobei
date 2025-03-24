N = int(input().strip())
count = 0

for i in range(1, N + 1):
    digits = list(map(int, str(i)))  # 将数字转换为整数列表
    good = True  # 记录是否为“好数”

    # 检查奇数位（个位、百位、万位...）
    for d in digits[::-2]:
        if d % 2 == 0:  # 发现偶数，直接标记为 False
            good = False
            break

    # 检查偶数位（十位、千位、十万位...）
    for d in digits[-2::-2]:
        if d % 2 == 1:  # 发现奇数，直接标记为 False
            good = False
            break

    if good:
        count += 1  # 计数加一

print(count)











# N = int(input().strip())
# count = 0
#
# for i in range(1, N + 1):
#   digits = list(map(int, str(i)))  # 将数字转换为整数列表
#
#   if any(d % 2 == 0 for d in digits[::-2]):  # 奇数位应该是奇数
#     continue
#   if any(d % 2 == 1 for d in digits[-2::-2]):  # 偶数位应该是偶数
#     continue
#
#   count += 1
#
# print(count)

# n=int(input())
# m=0
# for i in range (1,n+1):
#   while i>0 :
#     if i%2!=0 :
#       i=i//10
#     else:
#       break
#     if i%2==0:
#       i=i//10
#     else:
#       break
#     if i==0:
#       m+=1
# print(m)