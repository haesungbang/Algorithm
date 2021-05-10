# 11959. 최소 이동거리

def dijkstra(start):
    U = [0] * (N + 1)
    D = [987654321] * (N + 1)
    U[start] = 1
    D[start] = 0

    for next_node, weight in graph[start]:
        D[next_node] = weight

    for _ in range(N - 1):
        min_weight = 987654321
        for i in range(N):
            if not U[i] and D[i] < min_weight:
                min_weight = D[i]
                node = i

        U[node] = 1
        for next_node, weight in graph[node]:
            if not U[next_node]:
                D[next_node] = min(D[next_node], D[node] + weight)

    return D[N]


T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
    print('#%d %d' % (t, dijkstra(0)))
