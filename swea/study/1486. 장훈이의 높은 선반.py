# 1486. 장훈이의 높은 선반

# 모든 부분집합을 다 구하는 것 같은 방식
for t in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    min_top = sum(H)
    for i in range(1 << N):
        if min_top == B:
            break
        top = 0
        for j in range(N):
            if i & (1 << j):
                top += H[j]
            if top > min_top:
                break
        if B <= top < min_top:
            min_top = top

    print('#%d %d' % (t, min_top - B))