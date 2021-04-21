# 1861. 정사각형 방
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    # print(check)
    check = [0] * N * (N+1)
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0 <= nr < N and 0 <= nc < N and rooms[i][j] + 1 == rooms[nr][nc]:
                    check[rooms[nr][nc]] = 1
    max_cnt = cnt = 0
    for i in range(len(check) - 1, -1, -1):
        # 연속적으로 있다면 cnt를 계속 늘려간다.
        if check[i]:
            cnt += 1
        # 연속이 끊기면 그 때까지를 비교한 후 다시 cnt=0 으로 초기화
        else:
            if cnt >= max_cnt:
                max_cnt = cnt
                room_num = i
            cnt = 0

    print('#%d %d %d' % (t, room_num, max_cnt + 1))
