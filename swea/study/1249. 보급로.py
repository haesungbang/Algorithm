# 다익스트라 / BFS
drc = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def BFS_time(sr, sc):
    times = [[10 ** 20] * N for _ in range(N)]
    times[sr][sc] = 0
    queue = [(sr, sc)]
    rp = 0
    while rp < len(queue):
        r, c = queue[rp]
        rp += 1
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                new_time = times[r][c] + data[nr][nc]
                if times[nr][nc] > new_time:
                    times[nr][nc] = new_time
                    queue.append((nr, nc))
    return times[N - 1][N - 1]


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    print('#%d %d' % (t, BFS_time(0, 0)))
