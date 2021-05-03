# 1795. 인수의 생일파티

def dijkstra(start, graph):
    D = [987654321] * (N + 1)
    D[start] = 0
    U = [0] * (N + 1)
    U[start] = 1

    for next_node, weight in graph[start]:
        D[next_node] = weight

    for _ in range(N - 1):
        min_idx = 0
        for i in range(1, N + 1):
            if not U[i] and D[i] < D[min_idx]:
                min_idx = i

        U[min_idx] = 1
        for next_node, weight in graph[min_idx]:
            if not U[next_node]:
                D[next_node] = min(D[next_node], D[min_idx] + weight)
    return D[1:]


T = int(input())
for t in range(1, T + 1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    graph_t = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append((y, c))
        graph_t[y].append((x, c))

    result = max(a + b for a, b in zip(dijkstra(X, graph), dijkstra(X, graph_t)))
    print('#%d %d' % (t, result))