
# 1씩 증가시켜 몇 번 안에 비밀번호를 맞출 수 있는가?

# 공백으로 input() 을 두 개 받는다. split 기본이 공백
P, K = map(int, input().split())

print(P-K+1)
