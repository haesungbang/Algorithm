# 새로운 불면증 치료법
# 민석아 그냥 좀 자라...

t = int(input())

for i in range(1, t+1):
    N = int(input())
    result = []
    # 어떤 공간에 숫자를 넣고, 숫자가 있으면 안 넣는다.
    x = 0
    while result != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        x += 1
        T = x * N
        while T > 0:
            k = T % 10
            if k not in result:
                # not in 이 안 되는 거구나... count로 0개라면 추가하는 방법으로 하자.
                result += [k]
                result.sort()
            T = T // 10

    print(T)

    




            
        

