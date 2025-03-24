n = int(input())
shanqiu = list(map(int, input().split()))  # 修改：将输入的山的高度转换为整数列表

count = 0
for i in range(n):
    for j in range(i + 1, n):
        max_shanqiu = max(shanqiu[i], shanqiu[j])
        for k in range(i + 1, j):
            if max_shanqiu < shanqiu[k]:
                break
        else:
            count += 1  # 修改：此处判断该对山是否满足条件并更新count

print(count)





# n=int(input())
# shanqiu = list(map(int, input().split()))  # 修改：将输入的山的高度转换为整数列表
# # print(shanqiu)
# count=0
# for i in range(n):
#     for j in range(i+1,n):
#         max_shanqiu=max(shanqiu[i],shanqiu[j])
#         for k in range(i+1,j):
#             if max_shanqiu<shanqiu[k]:
#                 break
#             else:
#                 count+=1
# print(count)