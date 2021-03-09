# 10200. 구독자 전쟁

T = int(input())
for t in range(1, T+1):
    n, a, b = map(int, input().split())

    max_num = a
    if a >= b:
        max_num = b

    min_num = (a+b) - n
    if min_num <= 0:
        min_num = 0

    print('#%d %d %d'%(t, max_num, min_num))