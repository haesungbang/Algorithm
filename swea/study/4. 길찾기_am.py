# 4. 길찾기
# DFS 를 활용한 길찾기

def DFS_am(am, sv, ev):
    visited = [0] * 101
    s = [sv]
    result = 0
    while len(s):
        n = s.pop()
        if n == ev:
            result = 1
            break
        elif not visited[n]:
            visited[n] = 1
            for i in range(101):
                if am[n][i] == 1 and visited[i] == 0:
                    s.append(i)
    return result

T = 10

for t in range(1, T+1):
    tc, e = map(int, input().split())
    ed = list(map(int, input().split()))
    edges = []
    for i in range(e):
        edges.append(ed[2*i: 2*i + 2])
    # print(edges)
    am = [[0]*101 for _ in range(101)]
    for sc, ec in edges:
        am[sc][ec] = 1

    ans = DFS_am(am, 0, 99)
    print(ans)