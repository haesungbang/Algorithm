# 11578. 그래프 경로 코드
# DFS 활용하기!!!

T = int(input())

def DFS_am(v, am, sv, ev):
    # vertex 의 개수 만큼에 맍는 방문 기록소 생성
    visited = [0] * (v+1)
    stack = [sv]
    result = 0
    # 모든 곳을 다 돈다.
    while len(s):
        n = stack.pop()
        if n == ev:
            result = 1
            break
        # 방문 하지 않았다면
        elif not visited[n]:
            visited[n] = 1
            # 다 돌면서 스택 추가하고 반복
            for i in range(1, v+1):
                if am[n][i] == 1 and visited[i] == 0:
                    stack.append(i)
    return result

for t in range(1, T+1):
    v, e = map(int, input().split())
    # edges 이동하는 루트 만들기
    edges = [list(map(int, input().split())) for _ in range(e)]
    # am 만들기
    am =[[0]*(v+1) for _ in range(v+1)]
    # am 에 1 찍기
    for sc, ec in edges:
        am[sc][ec] = 1
    sv, ev = map(int, input().split())
    ans = DFS_am(v, am, sv, ev)
    print(ans)
