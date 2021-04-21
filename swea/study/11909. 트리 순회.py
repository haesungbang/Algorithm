# 11909. 트리순회(전, 중, 후)
def allorder(node):
    pre_visited.append(node)
    if tree[node][1] != 0:
        allorder(tree[node][1])
    in_visited.append(node)
    if tree[node][2] != 0:
        allorder(tree[node][2])
    back_visited.append(node)


T = int(input())
for t in range(1, T+1):
    V = int(input())
    # 값, 자식, 자식, 부모를 갖는 트리를 만든다.
    tree = [[k, 0, 0, 0] for k in range(V+1)]
    E = list(map(int, input().split()))
    for i in range(V-1):
        if not tree[E[2*i]][1]:
            tree[E[2 * i]][1] = E[2 * i + 1]
        else:
            tree[E[2 * i]][2] = E[2 * i + 1]
        tree[E[2*i+1]][3] = E[2*i]
    pre_visited = []
    in_visited = []
    back_visited = []
    allorder(1)
    p = '-'.join(map(str, pre_visited))
    i = '-'.join(map(str, in_visited))
    b = '-'.join(map(str, back_visited))

    print('#%d\n%s\n%s\n%s'%(t, p, i, b))
