import os
import sys

n = int(input())
res = set()  # 使用 set 提高查询效率
for i in range(n):
    m = input().split()
    if m[0] == 'I':
        res.add(m[1])  # 集合插入
    elif m[0] == 'Q':
        print("Yes" if m[1] in res else "No")






# import os
# import sys
# n=int(input())
# res=[]
# for i in range (n):
#   m=input().split()
#   if m[0]=='I':
#     res.append(m[1])
#   if m[0]=='Q':
#     if m[1] in res:
#       print("Yes")
#     else:
#       print("No")