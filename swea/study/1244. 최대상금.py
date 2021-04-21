# 1244. 최대상금
# 가장 뒤, 가장 큰 숫자랑 바꾸는 방법은 실패

def powernum(nums, k):
    global result, n
    if k == n:
        return
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            new_num = ''.join(nums)
            if new_num not in result:
                if k+1 == n:
                    result.append(new_num)
                powernum(nums, k+1)
            nums[i], nums[j] = nums[j], nums[i]

T = int(input())
for t in range(1, T+1):
    nums, n = input().split()
    nums = list(nums)
    n = int(n)
    result = []
    powernum(nums, 0)
    ans = max(result)
    print('#%d %s' %(t, ans))

# 왜 안되는 지 잘 모르겠습니다....
