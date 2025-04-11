# A = ['1','2','3','5','7']
# B = ['0','4','6','9']
# C = ['8']
# n=int(input())
# num=list(map(str,input().split()))
# def paixu(x):
#     s=0
#     for i in x:
#         if i in B:
#             s+=1
#         if i in C:
#             s+=2
#     return s,int(x)
# num.sort(key=paixu)
# print(" ".join(num))
#

n=int(input())
num=list(map(str,input().split()))
vl=[1,0,0,0,1,0,1,0,2,1]
id=0
a=[0]*n
k=[]
for i in range(n):
    for digit in num[i]:
        a[id]+=vl[int(digit)]
    k.append([a[id], int(num[i])])
    id+=1
k.sort(key=lambda x:(x[0],x[1]))
print(" ".join(str(x[1]) for x in k))


