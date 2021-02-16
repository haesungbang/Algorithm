# 숫자 배열 회전

T = int(input())

for t in range(1, T+1):
    N = int(input())
    result = [[''] * 3 for _ in range(N)]

    arr = list(list(map(str, input().split())) for _ in range(N))

    # result 의 0 열은 arr 의 열 순서대로 아래에서 위로 다 합친다.
    for i in range(N):
        for j in range(N-1, -1, -1):
            result[i][0] += arr[j][i]
    # print(result)

    # result 의 2 열은 arr 의 열 역순으로 위에서 아래로 다 합친다.
    for i in range(N-1, -1, -1):
        for j in range(N):
            result[N-i-1][2] += arr[j][i]
    # print(result)

    # result 의 1 열은 arr 의 행 역순으로 뒤에서 부터 앞으로 다 합친다.
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            result[N-i-1][1] += arr[i][j]
    # print(result)

    # 리스트 내에 리스트... 어떻게 정답처럼 만들 수 있을까요???

    print('# %d'%t)
    # 한 개씩 프린트...
    for i in range(N):
        print('%s'%(' '.join(result[i])))






