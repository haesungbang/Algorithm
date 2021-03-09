# 1225. 암호생성기 queue

for i in range(1, 11):
    t = int(input())
    queue = list(map(int, input().split()))
    turn = 1
    # 얼마나 반복할 것인지 모른다. break 로 나온다.
    while True:
        queue.append(queue.pop(0) - turn)
        if queue[-1] <= 0:
            queue[-1] = 0
            break
        if turn == 5:
            turn = 1
        else:
            turn +=1

    print(queue)


