# 4466. 최대 점수 만들기

T = int(input())

for t in range(1, T+1):
    n, k = map(int, input().split())
    scores = sorted(list(map(int, input().split())))
    result = sum(scores[-1:k*(-1)-1])
    print(result)