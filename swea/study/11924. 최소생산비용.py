# 11924. 최소 생산 비용
def DFS(level, total):
    global min_total
    # 이 경우의 수를 넣음으로 시간이 줄었다. 확인하자
    if total >= min_total:
        return
    if level == N:
        if min_total > total:
            min_total = total
        return
    # 반복문을 활용해서 여러가지 경우를 확인하자
    for c in range(N):
        if not visited[c]:
            visited[c] = 1
            DFS(level+1, total+arr[level][c])
            visited[c] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    visited = [0] * 15
    min_total = 98765432
    DFS(0, 0)
    print('#%d %d'%(t, min_total))