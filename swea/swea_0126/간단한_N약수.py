
# 간단한 N의 약수 구하기

# print 기본이 줄바꿈, 하지만 이렇게 풀었을 때는 틀릴 가능성이 있다.
N = int(input())

for i in range(N):
    if N%(i+1) == 0:
        print(i+1, end=' ')

# join 을 활용한 문제풀이
# 구분기호.join(list)
n = int(input())
divisor_list = []
for i in range(1, n + 1):
    if n % i == 0:
        divisor_list.append(str(i))
print(' '.join(divisor_list))