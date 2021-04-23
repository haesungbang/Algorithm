# 11928. DFS 연습

def DFS(s):
    visited[s] = 1
    result.append(s)
    for i in range(len(al[s])):
        if not visited[al[s][i]]:
            DFS(al[s][i])

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    al = [[] for _ in range(V+1)]
    for i in range(E):
        edge = list(map(int, input().split()))
        # 방향이 없으니까 양쪽에 다 넣어준다...
        al[edge[0]].append(edge[1])
        al[edge[1]].append(edge[0])
    visited = [0] * (V+1)
    result = []
    DFS(1)
    ans = ' '.join(map(str, result))
    print('#%d %s'%(t, ans))