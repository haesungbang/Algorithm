# 자기 방으로 돌아가기
# 통로를 하나의 길로 생각하고 지나가면 흔적을 남긴다.

T = int(input())

for t in range(1, T+1):
    rooms = [0] * 401
    n = int(input())
    mans = []
    for i in range(n):
        man = list(map(int, input().split()))
        mans.append(man)
    for s, e in mans:
        for i in range(s, e+1):
            rooms[i] += 1
    print(max(rooms))

