# 11634. 피자굽기

T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())
    cheese = list(map(int, input().split()))
    q = [i for i in range(n)]
    temp = n
    while len(q) > 1:
        a = q.pop(0)
        cheese[a] //= 2
        if cheese[a] > 0:
            q.append(a)
        elif temp < m:
            q.append(temp)
            temp += 1
    ans = q[0] + 1
    print('#%d %d'%(t, ans))



