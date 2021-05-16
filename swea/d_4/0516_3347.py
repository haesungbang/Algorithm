# 3347. 올림픽 종목투표

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    votes = [0] * N
    for b in B:
        for i in range(N):
            if A[i] <= b:
                votes[i] += 1
                break
    result = votes.index(max(votes)) + 1
    print('#%d %d' % (t, result))
