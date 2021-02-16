# 두 개의 숫자열
T = int(input())

for t in range(1, T+1):
    len_up, len_down = map(int, input().split())
    up_line = list(map(int, input().split()))
    down_line = list(map(int, input().split()))
    total_list = []
    
    if len_up > len_down:
        for i in range(len_up - len_down + 1):
            total = 0
            for j in range(len_down):
                total += down_line[j] * up_line[i+j]
            total_list.append(total)
    else:
        for i in range(len_down - len_up + 1):
            total = 0
            for j in range(len_up):
                total += down_line[j+i] * up_line[j]
            total_list.append(total)
    # print(total_list)
    
    # 초기값을 사용하기 위해 list의 결과들을 담고, 첫번째 값을 초기값으로 정한다.
    result = total_list[0]
    # 초기값과 결과들의 비교를 통해 원하는 값을 추출한다.
    for k in range(1, len(total_list)):
        if total_list[k] >= result:
            result = total_list[k]
    print('#%d %d'%(t, result))

