# 2814. 최장경로

def DFS(n, cnt):
    global max_cnt
    # 그냥 cnt 가 더 크면 계속 바꿔줘라
    if max_cnt < cnt:
        max_cnt = cnt
    # 방문
    visited[n] = 1
    # 반복문으로 돌린다
    for i in al[n]:
        if not visited[i]:
            DFS(i, cnt+1)
    visited[n] = 0

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    al = [[] for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        al[a].append(b)
        al[b].append(a)
    visited = [0] * (V+1)
    max_cnt = 0
    for i in range(V):
        DFS(i, 1)
    print('#%d %d'%(t, max_cnt))
