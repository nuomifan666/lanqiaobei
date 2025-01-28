from collections import deque
#1.28


def bfs(maze, start, end, N, M):
    # 定义四个方向（上、下、左、右）
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 队列，存储当前位置和当前步数
    queue = deque([(start[0], start[1], 0)])

    # 记录访问过的节点
    visited = [[False] * M for _ in range(N)]
    visited[start[0]][start[1]] = True

    while queue:
        x, y, dist = queue.popleft()

        # 如果到达终点，返回步数
        if (x, y) == end:
            return dist

        # 遍历四个方向
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 检查新位置是否合法
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    # 如果无法到达终点，返回-1
    return -1


def main():
    # 输入读取
    N, M = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(N)]
    x1, y1, x2, y2 = map(int, input().split())

    # 注意坐标是从1开始的，要转成从0开始的坐标
    start = (x1 - 1, y1 - 1)
    end = (x2 - 1, y2 - 1)

    # 如果起点或终点是障碍物，直接返回-1
    if maze[start[0]][start[1]] == 0 or maze[end[0]][end[1]] == 0:
        print(-1)
    else:
        # 调用BFS算法
        result = bfs(maze, start, end, N, M)
        print(result)


if __name__ == "__main__":
    main()
