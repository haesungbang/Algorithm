# 1206.view

for test_case in range(1, 10 + 1):
    T = int(input())
    l = list(map(int, input().split()))
    count = 0
    for i in range(2, len(l) - 2):
        neighbor = max(l[i - 2], l[i - 1], l[i + 1], l[i + 2])
        good_rooms = max(0, l[i] - neighbor)
        count = count + good_rooms

    print("#%d %d" % (test_case, count))