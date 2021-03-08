# Sum

for t in range(1, 11):
    tc = int(input())
    nums = [list(map(int, input().split())) for _ in range(100)]
    result = []
    # 가로, 세로
    for i in range(100):
        total_r = 0
        total_c = 0
        for j in range(100):
            total_r += nums[i][j]
            total_c += nums[j][i]
        result.append(total_r)
        result.append(total_c)
    # 대각선
    total_cross = 0
    for i in range(100):
        total_cross += nums[i][i]
    result.append(total_cross)
    ans = max(result)
    print('#%d %d' % (tc, ans))