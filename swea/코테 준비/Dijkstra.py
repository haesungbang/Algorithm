
def dijkstra(start):
    visited[start] = 1
    for adj_node, weight in arr[start]:
        D[adj_node] = weight

    # 가중치가 가장 적은 것을 찾는다.
    for k in range(N-1):
        min_weight = 999
        for i in range(N):
            if not visited[i] and D[i] < min_weight:
                min_weight = D[i]
                node = i
        # 가중치가 가장 적은 점을 방문
        visited[node] = 1
        for adj_node, weight in arr[node]:
            if not visited[adj_node]:
                D[adj_node] = min(D[adj_node], D[node] + weight)
                print(D)


T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    arr = [[] for _ in range(N+1)]
    for i in range(E):
        s, e, w = input().split()
        arr[ord(s) - 97].append([ord(e) - 97, int(w)])
    print(arr)
    visited = [0] * N
    D = [0] + [999] * (N-1)
    dijkstra(0)
    print(D)