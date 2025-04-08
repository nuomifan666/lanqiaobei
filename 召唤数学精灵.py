count,sum_res, = 0,0
fac_res = 1

for i in range(1, 1000):
    sum_res += i
    fac_res *= i
    if (sum_res - fac_res) % 100 == 0:
        print(f"i = {i}, sum = {sum_res}, fac = {fac_res}")
        count += 1

print("count =", count)
