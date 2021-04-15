# 두 수의 덧셈
T = int(input())
for t in range(1, T+1):
    a, b = map(int, input().split())
    # lambda 활용법
    plus = lambda x,y: x+y
    print('#%d %d'%(t, plus(a, b)))
