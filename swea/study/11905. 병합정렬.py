# merge_sort

def merge_sort(nums):
    global cnt
    if len(nums) == 1:
        return nums
    mid = len(nums)//2
    arr = merge_sort(nums[:mid])
    brr = merge_sort(nums[mid:])

    if arr[-1] > brr[-1]:
        cnt += 1

    result = []
    ai = 0
    bi = 0
    while ai < len(arr) and bi < len(brr):
        if arr[ai] > brr[bi]:
            result.append(brr[bi])
            bi += 1
        else:
            result.append(arr[ai])
            ai += 1
    # append 가 아니라 extend : 원소를 넣는거니까!!
    result.extend(arr[ai:])
    result.extend(brr[bi:])
    return result

T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    ans = merge_sort(nums)
    print(ans, cnt)