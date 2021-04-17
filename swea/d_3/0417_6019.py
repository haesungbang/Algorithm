# 6019. 기차사이의 파리
T = int(input())
for t in range(1, T+1):
    d, a, b, f = map(int, input().split())
    sec = d/(a+b)
    ans = f * sec
    print('#%d %d'%(t, ans))
