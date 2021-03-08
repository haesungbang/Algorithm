# 제곱 회문

for t in range(1, int(input()) + 1):
    s, e = map(int, input().split())
    result = 0
    for i in range(s, e+1):
        root_i = i ** (1/2)
        if root_i - int(root_i) == 0:
            if str(i) == str(i)[::-1] and str(int(root_i)) == str(int(root_i))[::-1]:
                result += 1
    print('#%d %d'%(t, result))