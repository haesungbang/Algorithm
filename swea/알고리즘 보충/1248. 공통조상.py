# 1248. 공통조상

# 공통조상 구하기
def get_root_a(sa):
    if tree[sa][2]:
        na = tree[sa][2]
        a_list.append(na)
        get_root_a(na)

def get_root_b(sb):
    if tree[sb][2]:
        nb = tree[sb][2]
        b_list.append(nb)
        get_root_b(nb)

# 공통조상 아래 노드의 개수
def backorder(root):
    for i in tree[root][:2]:
        if i != 0:
            backorder(i)
    visited.append(i)

T = int(input())
for t in range(1, T+1):
    V, E, a, b = map(int, input().split())
    # 자식, 자식, 부모, 값
    tree = [[0, 0, 0, i] for i in range(V+1)]
    edges = list(map(int, input().split()))
    for i in range(E):
        if tree[edges[2*i]][0] != 0:
            tree[edges[2*i]][1] = edges[2*i+1]
        else:
            tree[edges[2*i]][0] = edges[2*i+1]
        tree[edges[2*i+1]][2] = edges[2*i]
    # 루트 찾기
    a_list = []
    b_list = []
    get_root_a(a)
    get_root_b(b)
    root = 0
    for i in a_list:
        if i in b_list:
            root = i
            break
    # 루트 내에 노드의 개수
    visited = []
    backorder(root)
    ans = len(visited)
    print('#%d %d %d'%(t, root, ans))