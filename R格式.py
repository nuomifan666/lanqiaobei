from decimal import Decimal,getcontext


getcontext().prec=10000
n, num = input().split()
n = int(n)
num = float(num)
ans = num * n ** n
print(f"{ans:.0f}")
