# 5162. 두가지 빵의 딜레마

T = int(input())
for t in range(1, T+1):
    a, b, c = map(int, input().split())
    result = c // b
    if a <= b:
        result = c // a
    print('#%d %d'%(t, result))