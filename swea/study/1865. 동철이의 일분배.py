# 1865. 동철이의 일분배
def DFS(level, per):
    global max_per
    if max_per >= per:
        return
    if level == N:
        if max_per < per:
            max_per = per
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            DFS(level+1, per*(P[level][i]/100))
            visited[i] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    P = list(list(map(int, input().split())) for _ in range(N))
    max_per = 0
    visited = [0]*N
    DFS(0, 1)
    # 반올림 round(실수, x)
    ans = round(max_per*100, 6)
    # 소수점 x자릿수 표현 %0.xf
    print('#%d %0.6f'%(t, ans))

