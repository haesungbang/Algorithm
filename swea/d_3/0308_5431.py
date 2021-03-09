# 5431. 민석이의 과제 관리

T = int(input())

for t in range(1, T+1):
    N, p = map(int, input().split())
    work = [0] * (N+1)
    do = list(map(int, input().split()))
    for i in range(p):
        work[do[i]] = 1

    result = []
    i = 1
    while i < N+1:
        if work[i] == 0:
            result.append(i)
        i += 1

    ans = ' '.join(map(str, result))
    print('#%d %s'%(t, ans))

