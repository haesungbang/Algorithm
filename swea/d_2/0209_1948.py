# 날짜 계산기
T = int(input())
for t in range(1, T+1):
    days = [31, 28, 31, 30, 31, 30,  31, 31, 30, 31, 30, 31]
    # month 가 순차적이기 때문에 list 를 활용한다.
    month_day = list(map(int, input().split()))
    start_mon = month_day[0]
    start_day = month_day[1]
    end_mon = month_day[2]
    end_day = month_day[3]
    gap_day = end_day - start_day + 1
    gap_mon = end_mon - start_mon
    gap_mon_day = 0
    result = 0
    # month 가 같다면 날짜의 차이
    if gap_mon == 0:
        result = gap_day
    # month 가 다르다면 start_mon 부터 end_mon 전 까지의 month 의 날짜를 더하고
    # 날짜의 차이를 추가적으로 더해준다.
    else:
        for i in range(gap_mon):
            gap_mon_day += days[start_mon + i - 1]
        result = gap_mon_day + gap_day
    
    print('#%d %d'%(t, result))