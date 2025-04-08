n,m=map(int,input().split())
grid=[list(map(int,input().split()))for _ in range(n)]
# for i in range(n):
# #     row=list(map(int,input().split()))
# #     grid.append(row)

count = 0
for a in range(n):
    for b in range(m):
        for c in range(n):
            for d in range(m):
                if grid[a][b] == grid[c][d] and abs(a - c) == abs(b - d) and abs(a - c) > 0:
                    count+=1
print(count)