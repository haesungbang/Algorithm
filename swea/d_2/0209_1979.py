# 어디에 단어가 들어갈 수 있을까?
# 하... 조금 더 해보자...
T = int(input())
for t in range(1, T+1):
    N , K = map(int, input().split())
    space =[]
    rotate_space = []
    for i in range(N):
        space.append(list(map(int, input().split())))
    print(space)
    cnt = 0
    for j in range(N):
        compare = [1] * K
        num = 0
        while N >= K + num:
            if space[j][num:K+num] == compare:
                cnt += 1
                num += K
            else:
                num += 1
    print(cnt)

