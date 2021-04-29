# 11946. 그룹나누기(find_set 활용하기)
# id 를 만지는 느낌이다. find_set 으로 id를 찾고 set으로 중복을 거른다.
def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    p = [i for i in range(N + 1)]
    for i in range(M):
        p[find_set(nums[2*i+1])] = find_set(nums[2*i])

    result = set()
    for i in p[1:]:
        result.add(find_set(i))
    print('#%d %d'%(t, len(result)))
