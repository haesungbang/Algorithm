# 11572. 괄호검사

T = int(input())
bracket = ['(', '{', '[', ')', '}', ']']
for t in range(1, T+1):
    case = list(map(str, input()))
    # print(case)
    s = []
    result = 1
    for i in case:
        # 왼쪽 괄호는 그냥 나오면 넣는다.
        for j in range(3):
            if i == bracket[j]:
                s.append(i)
                break
        # 오른쪽 괄호가 나오면 pop 후 검사한다.
        for j in range(3):
            if i == bracket[3+j]:
                if s.pop() != bracket[j]:
                    result = 0
    # 남아있는 것이 있다면 fail
    if len(s) != 0:
        result = 0

    print('#%d %d'%(t, result))


