# Flatten

for t in range(1, 11):
    dumps = int(input())
    box = list(map(int, input().split()))

    for dump in range(dumps):
        low = 101
        high = 0
        max_i = 0
        min_i = 0
        for i in range(len(box)):
            if box[i] < low:
                low = box[i]
                min_i = i
            if box[i] > high:
                high = box[i]
                max_i = i
        box[max_i] -= 1
        box[min_i] += 1

    ans = max(box) - min(box)
    print(ans)