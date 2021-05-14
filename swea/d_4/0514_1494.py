# 1494. 사랑의 카운슬러

def v(a, b):
    return (a * a) + (b * b)


def dfs(idx, cnt):
    global result

    if cnt == n // 2:
        x = 0;
        y = 0
        for i in range(n):
            if visit[i]:
                x += worm[i][0]
                y += worm[i][1]
            else:
                x -= worm[i][0]
                y -= worm[i][1]

        result = min(result, v(x, y))
        return

    for i in range(idx, n):
        if visit[i]: continue

        visit[i] = True
        dfs(i + 1, cnt + 1)
        visit[i] = False


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    worm = [list(map(int, input().split())) for _ in range(n)]
    visit = [False] * n
    result = float('inf')

    dfs(0, 0)
    print(f"#{tc} {result}")