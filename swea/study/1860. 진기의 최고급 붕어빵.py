# 1860. 진기의 최고급 붕어빵

T = int(input())

for t in range(1, T+1):
    n, m, k = map(int, input().split())
    # 오는 시간이 계속 증가하지는 않는다.
    man = sorted(list(map(int, input().split())))

    result = 'Impossible'
    for i in range(1, n+1):
        rest = k * (man[i] // m) - i
        if rest < 0:
            result = "Possible"
            break

    print('#%d %s'%(t, result))

