# 11578. 그래프 경로 코드
# DFS AL 활용하기!!!

T = int(input())

def DFS_al(v, al, sv, ev):
    visited = [0] * (v+1)
    stack = [sv]
    result = 0
    while len(stack):
        n = stack.pop()
        if n == ev:
            result = 1
            break
        elif not visited[n]:
            visited[n] = 1
            for i in al[n]:
                if visited[i] == 0:
                    stack.append(i)
    return result

for t in range(1, T+1):
    v, e = map(int, input().split())
    # edges 이동하는 루트 만들기
    edges = [list(map(int, input().split())) for _ in range(e)]
    # al 만들기
    al = [[] for _ in range(v+1)]
    for sc, ec in edges:
        al[sc].append(ec)
    sv, ev = map(int, input().split())
    ans = DFS_al(v, al, sv, ev)
    print(ans)
