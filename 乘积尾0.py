ans=1
for i in range(10):
    a = list(map(int, input().split()))
    for j in a:
        ans = ans * j
print(ans)
