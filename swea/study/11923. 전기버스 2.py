# 11923. 전기버스 2

def charge_cnt(idx, distance, k):
    global cnt
    if idx >= N-1:
        return
    if k >= cnt:
        return
    if distance <= charge[idx]:
        if k <= cnt:
            cnt = k
        return
    for i in range(charge[idx]):
        charge_cnt(idx+i+1, distance-i-1, k+1)

T = int(input())
for t in range(1, T+1):
    data = list(map(int, input().split()))
    N, charge = data[0], data[1:]
    cnt = 101
    charge_cnt(0, N-1, 0)
    print('#%d %d'%(t, cnt))