# 11907. 이진탐색
# 문제 잘 읽자...
def binarySearch(num):
    global cnt
    left, right = 0, N - 1
    status = 0
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == num:
            cnt += 1
            return
        elif A[mid] < num:
            if status == 1:
                return
            status = 1
            left = mid + 1
        elif A[mid] > num:
            if status == -1:
                return
            status = -1
            right = mid - 1
    return

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for num in B:
        binarySearch(num)
    print('#%d %d' % (t, cnt))
