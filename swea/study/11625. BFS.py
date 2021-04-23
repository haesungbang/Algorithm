# 11625. BFS 연습

def BFS(s):
    q = [s]
    visited[s] = 1
    while q:
        n = q.pop(0)
        result.append(n)
        for i in al[n]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    al = [[] for _ in range(V+1)]
    for i in range(E):
        s, e = map(int, input().split())
        al[s].append(e)
        al[e].append(s)
    visited = [0] * (V+1)
    result = []
    BFS(1)
    print('#%d %s'%(t, ' '.join(map(str, result))))
