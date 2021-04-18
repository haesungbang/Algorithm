# 4371. 항구에 들어오는 배
T = int(input())
for t in range(1, T+1):
    N = int(input())
    happy_day = []
    for i in range(N):
        happy_day.append(int(input()))

    ships = [happy_day[1] - happy_day[0]]
    for i in range(2, N):
        a = happy_day[i] - happy_day[0]
        # 차이가 기록 날짜에 없다면
        if a not in ships:
            flag = 1
            # 나누어진다면 flag를 0으로 만들어 추가하지 않는다.
            for j in ships:
                if not a % j:
                    flag = 0
                    break
            if flag:
                ships.append(a)

    # print(ships)
    ans = len(ships)
    print('#%d %d'%(t, ans))
