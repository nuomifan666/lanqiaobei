n=int(input())
a=[0]+list(map(int,input().split()))
s=[0]*(n+1) #一开始没有+1
for i in range(1,n+1):
    s[i]=s[i-1]+a[i]

result=0
for j in range(1,n):
    result+=a[j]*(s[n]-s[j])

print(result)



import os
import sys
# n=int(input())
# arr=list(map(int,input().split()))
# ans=0
# for i in range(0,n):
#   for j in range(i+1,n):
#     ans+=arr[i]*arr[j]
# print(ans)