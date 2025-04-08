def zhuanhua(n,m):
    res=0
    while n>0:
        res+=n%m
        n=n//m
    return res
count=0
for i in range(1,2025):
    if zhuanhua(i,2)==zhuanhua(i,4):
        count+=1
print(count)