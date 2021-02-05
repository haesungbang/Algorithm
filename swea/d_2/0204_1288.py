# 새로운 불면증 치료법
# 민석아 그냥 좀 자라...

t = int(input())

for i in range(1, t+1):
    N = int(input())
    result = []
    # 어떤 공간에 숫자를 넣고, 숫자가 있으면 안 넣는다.
    cnt = 0
    while result != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    # 공간의 길이로 하는 법: while len(result) < 10:
        cnt += 1
        # 계속해서 곱해가면서 조건에 맞을 때까지 하는 방법
        num = cnt * N
        while num > 0:
            n = num % 10
            # if k not in result:
            if result.count(n) == 0:
            # 숫자가 있으면 안 넣는다 : count(n) == 0 이면 숫자가 안에 없다.
            # not in 이 안 되는 거구나... count로 0개라면 추가하는 방법으로 하자.
                result.append(n)
                result.sort()
            num = num // 10
    print(cnt * N)

    




            
        

