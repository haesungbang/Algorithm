# 10505. 소득불균형

T = int(input())

for t in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    avg_num = sum(num) / N
    cnt = 0
    for i in num:
        if num >= avg_num:
            cnt += 1

    print(cnt)