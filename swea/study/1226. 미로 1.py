# 1226. 미로 1

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

def start_point(miro):
    for i in range(n):
        for j in range(n):
            if miro[i][j] == 2:
                return i, j
def bfs(sr, sc):
    visited = [[0]*n for _ in range(n)]
    visited[sr][sc] = 1
    q = [(sr, sc)]
    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and miro[nr][nc] != 1:
                visited[nr][nc] = 1
                if miro[nr][nc] == 3:
                    return 1
                q.append((nr, nc))
    return 0


for t in range(1, 11):
    tc = int(input())
    n = 16
    miro = [list(map(int, input())) for _ in range(n)]
    sr, sc = start_point(miro)
    print(bfs(sr, sc))