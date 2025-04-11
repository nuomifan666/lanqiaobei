nums = [5160,9191,6410,4657,7492,1531,8854,1253,4520,9231,
        1266,4801,3484,4323,5070,1789,2744,5959,9426,4433,
        4404,5291,2470,8533,7608,2935,8922,5273,8364,8819,
        7374,8077,5336,8495,5602,6553,3548,5267,9150,3309]

total = sum(nums)
target = total // 2
dp = [False] * (target + 1)
dp[0] = True
max_sum = 0

for num in nums:
    for i in range(target, num-1, -1):
        if dp[i - num]:
            dp[i] = True
            if i > max_sum:
                max_sum = i

print(max_sum * (total - max_sum))
