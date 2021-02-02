
# 몫과 나머지 출력

t = int(input())

for i in range(t):

# 여러번 수를 입력해야되기 때문에 for 문 안에 넣어준다.
    a, b = map(int,input().split())
    
    print('#{} {} {}'.format(i+1, a//b, a%b))

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    print(f"#{test_case} {a // b} {a % b}")