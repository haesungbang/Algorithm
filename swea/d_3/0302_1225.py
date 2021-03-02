# 1225. 암호생성기

T = 1

for t in range(1, T+1):
    tc = int(input())
    num = list(map(int, input().split()))

    i = 1
    while:
        for j in range(5):
            k = num.pop(0) - (i+j)
            if k < 0:
                k = 0
                num.append(k)
                break
            else:
                num.append(k)
        else:
            i = 1
        ans = ' '.join(map(str, num))
    print('#%d %s'%(tc, ans))


