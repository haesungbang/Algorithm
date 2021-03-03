# sw10 비밀번호

T = 10

for t in range(1, T+1):
    n, nums = input().split()
    N = int(n)
    pwd = []
    for i in range(N):
        if len(pwd) == 0:
            pwd.append(nums[i])
        elif pwd[-1] != nums[i]:
            pwd.append(nums[i])
        else:
            pwd.pop()
    ans = ' '.join(pwd)
    print('#%d %s'%(t, ans))
