
# 대각선으로 '#'을 그리시오.

# for 와 format 활용하기
for i in range(5):
    a = '+'*i
    b = '#'
    c = '+'*(5-i)
    print(f'{a}{b}{c}')

# list 와 insert 활용하기

for i in range(5):
    n = ['+', '+', '+', '+']
    n.insert(i, '#')
    print(''.join(n))
