def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)


def kruskal():
    weight = 0
    for s, e, w in graph:
        rep_s, rep_e = find_set(s), find_set(e)
        if rep_s != rep_e:
            weight += w
            union(s, e)
    return weight


T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    p = [i for i in range(V + 1)]
    graph = sorted([list(map(int, input().split())) for x in range(E)], key=lambda x: x[2])
    print('#%d %d' % (t, kruskal()))
