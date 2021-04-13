# 5603. 건초 더미
def avg(box):
    average = int(sum(box) / len(box))
    return average


def move(box, avg):
    global cnt
    for i in box:
        if i > avg:
            cnt += (i - avg)
        elif i < avg:
            cnt += (avg - i)
    cnt //= 2


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    box = []
    for i in range(N):
        a = int(input())
        box.append(a)

    cnt = 0
    avg_box = avg(box)
    move(box, avg_box)
    print('#%d %d' % (t, cnt))