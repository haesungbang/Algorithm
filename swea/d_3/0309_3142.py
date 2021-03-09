# 3142. 영준이의 신비한 뿔의 숲

T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())
    total = m * 2
    i = 0
    while total - i > n:
        i += 1
    one = i
    two = m - i
    print('#%d %d %d'%(t, one, two))