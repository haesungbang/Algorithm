# 가랏!RC카

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    first_v = 0
    distance = 0
    for i in range(N):
        command = list(map(int, input().split()))
        if command[0] == 1:
            first_v += command[1]
            distance += first_v
        elif command[0] == 2:
            first_v -= command[1]
            if first_v < 0:
                first_v = 0
            distance += first_v
        elif command[0] == 0:
            distance += first_v
    print(distance)
