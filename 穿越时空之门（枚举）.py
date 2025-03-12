def tr(n,base):
    sum=0
    while n>0:
        sum+=n%base
        n=n//base
    return sum

count=0
for i in range(1,2025):
    if tr(i,2)==tr(i,4):
        count+=1
print(count)
