ans = 0
n = 2021041820210418
lst = []
for i in range(1,int(n**0.5)+1):
    if (n % i == 0):
        lst.append(i)
        if n / i != i:
            lst.append(n/i)

for i in lst:
    for j in lst:
        for k in lst:
            if (i*j*k == n):
                ans += 1
print(ans)
