# 수도 요금

t = int(input())
# a사 P * W  b사 Q + S(W-R) 
for i in range(1, t+1):
    P, Q, R, S, W = map(int, input().split())
    a = P * W
    if W - R <= 0:
        b = Q
    else:
        b = Q + S*(W-R)
    
    if a < b:
        print(f"#{i} {a}")
    else:
        print(f"#{i} {b}")
    