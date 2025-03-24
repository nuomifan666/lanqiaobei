n=int(input())
num=list(map(int,input().split()))
count=0
for i in range(1,n):
    if num[i]>num[i-1]:
        continue
    else:
        count+=num[i-1]-num[i]+1
        num[i]=num[i-1]+1
print(count)