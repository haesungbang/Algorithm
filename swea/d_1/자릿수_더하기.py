
# 자릿수를 더해라 (string 이 순서가 있는 것을 이용)

num = input()
int_num = int(num)
_sum = 0

for i in range(len(num)):
    _sum += int(num[i])

print(_sum)

# 자릿수를 더해라 (몫을 이용)

num = int(input())
_sum = 0

while num > 0:
    _sum += num%10
    num = num//10

# num은 몫이니까 몫이 0이되면 while 반복이 되지 않는다.

print(_sum)