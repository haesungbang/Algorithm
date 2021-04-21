# 2819. 격자판에 숫자 이어붙이기
# set()을 활용하는 것이 훨씬 빠르다.
'''
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def make_num(level, r, c, num):
    if level == 7:
        # set() 은 add로 더한다.
        result.add(num)
        return

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0<=nr<4 and 0<=nc<4:
            make_num(level+1, nr, nc, num+arr[nr][nc])


T = int(input())
for t in range(1, T+1):
    arr = list(list(input().split()) for _ in range(4))
    # set()은 애초에 중복된 것은 안 넣는다.
    result = set()
    for i in range(4):
        for j in range(4):
            make_num(1, i, j, arr[i][j])
    print(len(result))
'''
# 2819. 격자판에 숫자 이어붙이기
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def make_num(num, r, c):
    num += arr[r][c]
    if len(num) == 7:
        if num not in result:
            result.append(num)
        return
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0<=nr<4 and 0<=nc<4:
            make_num(num, nr, nc,)

T = int(input())
for t in range(1, T+1):
    arr = list(list(input().split()) for _ in range(4))
    # set()은 애초에 중복된 것은 안 넣는다.
    result = []
    for i in range(4):
        for j in range(4):
            make_num('', i, j)
    print(len(result))