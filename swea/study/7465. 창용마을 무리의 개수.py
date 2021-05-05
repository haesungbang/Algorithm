# 7465. 창용마을 무리의 개수
def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    p = [i for i in range(N + 1)]
    for _ in range(M):
        s, e = map(int, input().split())
        p[find_set(e)] = find_set(s)
    cnt = 0
    for i in range(1, N + 1):
        if i == find_set(i):
            cnt += 1

    print('#%d %d' % (t, cnt))