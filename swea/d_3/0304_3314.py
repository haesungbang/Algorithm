# 3314. 보충학습과 평균

T = int(input())

for t in range(1, T+1):
    score = list(map(int, input().split()))
    for i in range(len(score)):
        if score[i] < 40:
            score[i] = 40
    print(score)
    result = sum(score) / len(score)
    print('#%d %d'%(t, int(result)))