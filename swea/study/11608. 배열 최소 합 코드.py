# 116083 배열 최소 합 코드
# 아래로 쭉 내려가면서 확인하는 것 보니 dfs 느낌이 온다.
# 무슨 뜻인지 잘 모르겠다... 설명 듣자

def DFS(level):

    global min_num
    sum_num = 0
    for k in range(level):
        sum_num += nums[k][arr[k] - 1]
        if sum_num > min_num:
            return

    if level == n:
        min_num = sum_num
        return

    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = 1
        arr[level] = i
        DFS(level + 1)
        arr[level] = 0
        visited[i] = 0

for t in range(1, int(input())+1):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * (n + 1) # 방문 표시
    arr = [0] * n # 층마다 선택된 숫자 위치를 저장하는 곳
    min_num = 50
    DFS(0)
    print('#%d %d' % (t, min_num))


'''
def DFS(level):
    global min_sum
    arr_sum = 0
    for i in range(level):
        arr_sum += nums[i][arr[i]-1]
        if arr_sum > min_sum:
            return
    # 종료 조건
    if level == n:
        min_sum == arr_sum
        return
    # DFS 확산
    for j in range(1, n + 1):
        if visited[j]:
            continue
        visited[j] = 1
        arr[level] = j
        DFS(level + 1)
        visited[j] = 0

for t in range(1, int(input())+1):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * (n + 1) # 방문 표시
    arr = [0] * n # 선택된 숫자를 저장하는 배열
    min_sum = 50
    DFS(0)
    print('#%d %d' % (t, min_sum))
'''