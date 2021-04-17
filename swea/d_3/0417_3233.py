# 3233. 정삼각형 분할놀이

T = int(input())
for t in range(1, T+1):
    a, b = map(int, input().split())
    print('#%d %d'%(t, (a//b)**2))