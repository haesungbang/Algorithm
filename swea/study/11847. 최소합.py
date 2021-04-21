# 11847. 최소합

# BFS
dr = [1, 0]
dc = [0, 1]

def BFS(sr, sc):
    q = [(sr, sc)]
    result[sr][sc] = cost[0][0]
    while q:
        r, c = q.pop(0)
        for i in range(2):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                temp = result[r][c] + cost[nr][nc]
                if temp < result[nr][nc] or not result[nr][nc]:
                    result[nr][nc] = temp
                    q.append((nr, nc))

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    result = [[0]*N for _ in range(N)]
    BFS(0, 0)
    print('#%d %d'%(t, result[N-1][N-1]))


# BFS X
'''
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 가장 위쪽, 왼쪽을 다 채워준다.
    for i in range(1, N):
        arr[0][i] += arr[0][i - 1]
        arr[i][0] += arr[i - 1][0]

    for i in range(1, N):
        for j in range(1, N):
            arr[i][j] += min(arr[i - 1][j], arr[i][j - 1])
    ans = arr[N - 1][N - 1]
    print('#%d %d' % (t, ans))
'''