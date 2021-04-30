def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


def kruskal():
    result = 0
    cnt = 0
    for weight, node1, node2 in graph:
        if find_set(node1) != find_set(node2):
            union(node1, node2)
            result += weight
            cnt += 1
            if cnt == N - 1:
                break
    return result


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    p = [i for i in range(N)]
    graph = []
    for i in range(N):
        for j in range(i + 1, N):
            weight = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
            graph.append((weight, i, j))
    graph.sort()
    print('#%d %d' % (t, round(kruskal() * E)))
