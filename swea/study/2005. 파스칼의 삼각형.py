# 2005. 파스칼의 삼각형

T = int(input())

for t in range(1, T+1):
    N = int(input())
    result = []
    # 1 을 요소로 갖는 증가하는 크기의 공간을 만들어서 추가한다.
    for i in range(1, N+1):
        line = []
        for j in range(i):
            line.append(1)
        result.append(line)

    # 2 이상인 경우 아래 수식을 적용해서 값을 바꾼다.
    i = 2
    while i < N:
        for j in range(i-1):
            result[i][j+1] = result[i-1][j] + result[i-1][j+1]
        i += 1

    print('#%d'%t)
    for i in range(N):
        print(' '.join(map(str, result[i])))
