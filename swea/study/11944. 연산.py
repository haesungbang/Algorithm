# 11944. 연산
def calc(N):
    memo = [0] * (10 ** 6 + 1)
    queue = [0] * (10 ** 6 + 1)
    wp, rp = 0, -1
    queue[0] = (N, 0)
    memo[N] = 1
    while wp != rp:
        rp += 1
        target, cnt = queue[rp]
        tmp = [target + 1, target - 1, target * 2, target - 10]
        for t in tmp:
            if t == M:
                return cnt + 1
            elif 0 < t <= 10 ** 6 and memo[t] == 0:
                wp += 1
                queue[wp] = (t, cnt + 1)
                memo[t] = 1


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    print("#%d %d" % (t, calc(N)))
