# 시각 덧셈
'''
T = int(input())

for t in range(1, T+1):
    fh, fm, sh, sm = map(int, input().split())
    # hour
    hour = fh + sh
    # minute
    minute = fm + sm

    if minute > 59:
        minute -= 60
        hour += 1

    if hour > 12:
        hour -= 12

    print('#%d %d %d'%(t, hour, minute))
'''

# 몫과 나머지를 활용할 수도 있구나...
T = int(input())

for t in range(1, T+1):
    fh, fm, sh, sm = map(int, input().split())

    hour = (fh + sh) % 12 + (fm + sm) // 60
    minute = (fm + sm) % 60

    print('#%d %d %d' % (t, hour, minute))

