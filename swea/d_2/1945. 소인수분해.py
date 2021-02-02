num = int(input())
for i in range(1,num+1):
    N = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while N%2 == 0:
        a += 1
        N = N//2
    while N%3 == 0:
        b += 1
        N = N//3
    while N%5 == 0:
        c += 1
        N = N//5
    while N%7 == 0:
        d += 1
        N = N//7
    while N%11 == 0:
        e += 1
        N = N//11
    
    print(f"#{i} {a} {b} {c} {d} {e}")
    