# 어디에 단어가 들어갈 수 있을까?

T = int(input())
for t in range(1, T+1):
    N , K = map(int, input().split())
    space =[0] * N
    for i in range(N):
        space[i] = list(map(int, input().split()))
    # print(space)
    cnt = 0
    for j in range(N):
        compare = [1] * K
        for num in range(N - K + 1):
            if space[j][num:K+num] == compare:
                cnt += 1
                num += K
    print(cnt)

