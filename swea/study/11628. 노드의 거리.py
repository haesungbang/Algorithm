# 11628. 노드의 거리
def BFS(s, g):
    visited = [0] * (v + 1)
    q = []
    visited[s] = 0
    q.append(s)
    while q:
        target = q.pop(0)
        if target == g:
            return visited[target]

        for i in al[target]:
            if visited[i]:
                continue
            visited[i] = visited[target] + 1
            q.append(i)

T = int(input())

for t in range(1, T + 1):
    v, e = map(int, input().split())
    al = [[] for i in range(v+1)]
    for i in range(e):
        a, b = map(int, input().split())
        al[a].append(b)
        al[b].append(a)
    s, g = map(int, input().split())
    print(BFS(s, g))