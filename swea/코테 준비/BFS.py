
def BFS(start):
    visited[start] = 1
    visit = []
    q = [start]
    while q:
        n = q.pop(0)
        visit.append(n)
        for i in edges[n]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
    return visit

T = int(input())

for t in range(1, T+1):
    N, E = map(int, input().split())
    # 여러 공간 나타낼 때...
    visited = [0] * (N+1)
    edges = [[] for _ in range(N+1)]
    for i in range(E):
        s, e = map(int, input().split())
        edges[s].append(e)
        edges[e].append(s)
    start = 1
    # print(edges)
    ans = '-'.join(map(str, (BFS(start))))
    print(ans)

