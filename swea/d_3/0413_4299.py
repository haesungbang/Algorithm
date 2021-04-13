# 태혁이의 빼빼로데이
def paparo(time):
    ans = 0
    for i in range(len(time)):
        time[i] -= 11
        if (2-i)//2:
            ans += time[i] * 24 * 60
        elif i!=2:
            ans += time[i] * 60
    if ans < 0:
        return -1
    return ans

T = int(input())
for t in range(1, T+1):
    time = list(map(int, input().split()))
    # print(time)
    result = paparo(time)
    print('#%d %d'%(t, result))
