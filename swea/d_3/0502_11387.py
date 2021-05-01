# 11387. 몬스터 사냥

def damage(n):
    global D, L
    global result
    dam = D + D*n*L/100
    result += dam


T = int(input())
for t in range(1, T+1):
    # 데미지, 퍼센트, 횟수
    D, L, N = map(int, input().split())
    result = 0
    for i in range(N):
        damage(i)
    print('#%d %d'%(t, round(result)))
