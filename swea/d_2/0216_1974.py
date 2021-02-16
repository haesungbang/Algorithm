# 스도쿠 검증

T = int(input())
compare = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 반시계 방향으로 돌릴꺼다
dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, 1, 1, 0, -1, -1, -1, 0, 1]

for t in range(1, T+1):
    N = 9
    arr = list(list(map(int, input().split())) for _ in range(N))


    # line 검증
    # 이게 들어있는지 어떻게 확인할 수 있을까?
    cnt_line = 0
    for i in range(N):
        temp_r = []
        temp_c = []
        for j in range(N):
            temp_r.append(arr[i][j])
            temp_c.append(arr[j][i])
        if sorted(temp_r) == compare:
            cnt_line += 1
        if sorted(temp_c) == compare:
            cnt_line += 1
    # print(cnt_line)

    # box 검증
    cnt_box = 0
    for i in range(3):
        for j in range(3):
            temp_box = []
            for k in range(len(dr)):
                temp_box.append(arr[3*i + 1 + dr[k]][3*j + 1 + dc[k]])
            if sorted(temp_box) == compare:
                cnt_box += 1
    # print(cnt_box)

    if cnt_box + cnt_line == 27:
        print('#%d 1'%t)
    else:
        print('#%d 0'%t)