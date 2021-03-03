# 11556. 부분집합의 합
# 이진탐색을 통한 powerset...

T = int(input())

for t in range(1, T+1):
    a = []
    result = 0
    for i in range(1, 13):
        a.append(i)
    n, tot = map(int, input().split())
    result = 0
    # 이진탐색! 다시 한 번 봐두자!
    for i in range(1 << 12):
        part = []
        for j in range(12):
            if i & (1 << j):
                part.append(a[j])
        if sum(part) == tot and len(part) == n:
            result = 1
            break
    print(result)