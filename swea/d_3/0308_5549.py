# 5549. 홀수일까 짝수일까

def even_odd(num_list):
    if num_list[-1]%2 == 0:
        return 'Even'
    return 'Odd'

T = int(input())
for t in range(1, T+1):
    num = list(map(int, input()))
    # print(num)
    ans = even_odd(num)
    print('#%d %s'%(t, ans))
