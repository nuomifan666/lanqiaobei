a=set()
num=0
shu=["2","0","1","9"]
for i in range(1,2020):
    for num in str(i):
        if num in shu:
            a.add(i)
ans=sum(a)
print(ans)