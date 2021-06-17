def min_create(level, total):
    global min_total
    if total >= min_total:
        return
    if level == N:
        if min_total > total:
            min_total = total
        return
    for k in range(N):
        if not visited[k]:
            visited[k] = 1
            min_create(level+1, total+arr[level][k])
            # 초기화를 해준다.
            visited[k] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    visited = [0] * N
    min_total = 987654321
    min_create(0, 0)
    print(min_total)