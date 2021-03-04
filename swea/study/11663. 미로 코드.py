# 11663. 미로 거리 코드

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

def start_point(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                # 튜플형태로 가져와 진다.
                return [i, j]

def BFS(x, y):
    visited = [[0]*n for _ in range(n)]
    q = [(x, y)]
    visited[x][y] = 0
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx, ny = x + dr[i], y + dc[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maze[nx][ny] != '1':
                visited[nx][ny] = visited[x][y] + 1
                if maze[nx][ny] == '3':
                    return visited[nx][ny] - 1
                q.append((nx, ny))
    return 0

T = int(input())

for t in range(1, T+1):
    n = int(input())
    maze = [list(input())for _ in range(n)]
    # print(maze)
    start = start_point(maze)
    # print(start)
    print(BFS(start[0], start[1]))