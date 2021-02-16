# 직사각형 길이 구하기

T = int(input())

for t in range(1, T+1):
    len_square = list(map(int, input().split()))
    if len_square[0] == len_square[1]:
        result = len_square[2]
    elif len_square[0] == len_square[2]:
        result = len_square[1]
    elif len_square[1] == len_square[2]:
        result = len_square[0]

    print('#%d  %d'%(t, result))