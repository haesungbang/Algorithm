
# a b 를 입력받아 간단한 사칙연산을 출력해라.

# 공백으로 두 문자를 입력하기 위해서 .split() 을 사용한다.
a, b = map(int, input().split())

print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
