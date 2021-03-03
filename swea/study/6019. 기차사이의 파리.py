# 6019. 기차사이의 파리
# 10초 동안 파리가 날아가는 거리
T = int(input())

for t in range(1, T+1):
    d, a, b, f = map(int, input().split())
    result = (d/(a+b)) * f
    print(result)