# 5514. 2016년 요일 맞추기

days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())
for t in range(1, T+1):
    m, d = map(int, input().split())
    start_day = 5
    day = (start_day + sum(days[0:m-1]) + d) % 7
    print(day)
