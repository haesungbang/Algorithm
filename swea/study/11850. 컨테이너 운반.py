# 11850. 컨테이너
'''
def max_weight():
    global max_cargo
    while trucks:
        if not len(cargos):
            break
        weight = trucks.pop(0)
        max_w = 0
        max_idx = 0
        # 꼭 다 돌 필요가 없구나...
        for i in range(len(cargos)):
            if weight >= cargos[i] and max_w <= cargos[i]:
                max_w = cargos[i]
                max_idx = i
        cargos.pop(max_idx)
        max_cargo += max_w
'''

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    cargos = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)
    ci, ti = 0, 0
    max_cargo = 0
    while ci < N and ti < M:
        if trucks[ti] >= cargos[ci]:
            max_cargo += cargos[ci]
            ti += 1
            ci += 1
        else:
            ci += 1
    print('#%d %d'%(t, max_cargo))
