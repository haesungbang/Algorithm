drc = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def start(arr, n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                return i, j


def dfs_miro(arr, sv):
    stack = [sv]
    while stack:
        nr, nc = stack.pop()
        if visited[nr][nc] == 0:
            visited[nr][nc] = 1
            if arr[nr][nc] == 3:
                return 1
            for dr, dc in drc:
                nxr = nr + dr
                nxc = nc + dc
                if arr[nxr][nxc] != 1 and visited[nxr][nxc] == 0:
                    stack.append((nxr, nxc))
    return 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    miro = [[1] + list(map(int, input())) + [1] for _ in range(N)]
    miro.insert(0, [1] * (N + 2))
    miro.append([1] * (N + 2))
    visited = [[0] * (N + 2) for _ in range(N + 2)]
    miro_start = start(miro, N + 2)
    ans = dfs_miro(miro, miro_start)
    print('#%d %d' % (test_case, ans))