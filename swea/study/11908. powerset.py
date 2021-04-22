# 11908. powerset
# 재귀 함수
def get_powerset(idx, S):
    global cnt
    if S == M:
        cnt += 1
        return
    if S > M or idx >= N:
        return
    get_powerset(idx+1, S+nums[idx])
    get_powerset(idx+1, S)

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    cnt = 0
    get_powerset(0, 0)
    print('#%d %d'%(t, cnt))


'''
# 이진탐색
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    cnt = 0
    for i in range(1<<N):
        powerset = []
        for j in range(N):
            # and 가 아니라 & 를 써야한다: x and y 가 있으면 x가 False면 x를 반환하고, x가 True면 y값을 반환한다.
            if i & (1<<j):
                powerset.append(nums[j])
        if sum(powerset) == M:
            cnt += 1
    print('#%d %d'%(t, cnt))
'''