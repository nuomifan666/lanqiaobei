n = int(input())
north = list(map(int, input().split()))
west = list(map(int, input().split()))

result = None

def backtrack(current_i, current_j, path, visited, row_counts, col_counts):
    global result
    if current_i == n-1 and current_j == n-1:
        if row_counts == west and col_counts == north:
            result = path.copy()
            return True
        return False
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for di, dj in directions:
        ni, nj = current_i + di, current_j + dj
        if 0 <= ni < n and 0 <= nj < n:
            num = ni * n + nj
            if num not in visited:
                if row_counts[ni] + 1 > west[ni]:
                    continue
                if col_counts[nj] + 1 > north[nj]:
                    continue
                visited.add(num)
                path.append(num)
                row_counts[ni] += 1
                col_counts[nj] += 1
                if backtrack(ni, nj, path, visited, row_counts, col_counts):
                    return True
                visited.remove(num)
                path.pop()
                row_counts[ni] -= 1
                col_counts[nj] -= 1
    return False

start_num = 0
start_i, start_j = 0, 0
path = [start_num]
visited = set(path)
row_counts = [0] * n
col_counts = [0] * n
row_counts[start_i] += 1
col_counts[start_j] += 1

backtrack(start_i, start_j, path, visited, row_counts, col_counts)

print(' '.join(map(str, result)))
