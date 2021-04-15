# 10580. 전봇대

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lines = []
    lines.append(list(map(int, input().split())))
    cnt = 0
    for i in range(N - 1):
        line = list(map(int, input().split()))
        for j in range(len(lines)):
            if lines[j][0] < line[0] and lines[j][1] > line[1]:
                cnt += 1
            elif lines[j][0] > line[0] and lines[j][1] < line[1]:
                cnt += 1
        lines.append(line)
    print('#%d %d' % (t, cnt))


