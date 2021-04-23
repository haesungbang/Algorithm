# 11924. Dijkstra
DEFAULT = 999

def dijkstra(s):
    # 1. 방문 표시
    U[s] = 1
    # 2. 한 번에 갈 수 있는 노드에 가중치를 입력
    for adj_node, weight in AL[s]:
        D[adj_node] = weight
    # 3. 인접 된 것들 중에서 가중치가 가장 적은 것을 찾는다.
    for _ in range(N-1):
        min_weight = DEFAULT
        for i in range(N):
            if not U[i] and D[i] < min_weight:
                min_weight = D[i]
                node = i
    # 4. 가중치가 작은 작은 정점을 방문
        U[node] = 1
        for adj_node, weight in AL[node]:
            # 방문을 안했다면! 기존 가중치랑 D[node] + weight 비교해서 작은 값을 담는다.
            if not U[adj_node]:
                D[adj_node] = min(D[adj_node], D[node] + weight)

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    AL = [[] for _ in range(N)]
    for _ in range(M):
        s, e, w = input().split()
        AL[ord(s) - 97].append((ord(e) - 97, int(w)))
    U = [0] * N
    D = [0] + [DEFAULT] * (N - 1)
    dijkstra(0)
    print('#%d %s' % (t, ' '.join(map(str, D))))