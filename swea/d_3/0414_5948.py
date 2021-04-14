# 5948. 7-3-5 게임

T = int(input())
for t in range(1, T+1):
    nums = list(map(int, input().split()))
    n = len(nums)
    total_list = []
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                total = nums[i] + nums[j] + nums[k]
                if total not in total_list:
                    total_list.append(total)
                else:
                    continue
    # set(total_list) 를 활용해서 중복을 제거할 수 있다.
    # set 은 순서가 없기 때문에 다시 리스트를 씌워준다.
    total_list.sort()
    ans = total_list[-5]
    print('#%d %d'%(t, ans))