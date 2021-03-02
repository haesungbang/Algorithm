# 5601. 쥬스나누기

T = int(input())

for t in range(1, T+1):
    N = int(input())
    result = []
    for i in range(N):
        result.append('1/%d'%N)
    ans = ' '.join(result)
    print('#%d %s'%(t, ans))
