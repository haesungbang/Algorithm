# 11556. 부분집합의 합_dfs
# 재귀를 사용 ( 가장 먼저 종료조건 )

a = list(range(1, 13))
an = 12
subset = [0] * an

def DFS_subset(level, S):
    # 종료 조건
    if level == an:
        if sum(subset) == N and S == K:
            global sol
            sol += 1
        return

    subset[level] = 1
    DFS_subset(level + 1, S + a[level])
    subset[level] = 0
    DFS_subset(level + 1, S)

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    sol = 0
    DFS_subset(0, 0)
    print('#%d %d'%(t, sol))

