def plus(N, obj):
    stack = []
    plus = []
    result = 0

    for i in range(N):
        if stack:
            if obj[i].isnumeric():
                stack.append(obj[i])
            else:
                plus.append(obj[i])
            if len(stack) == 2:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a + b)
        else:
            stack.append(obj[i])
    return stack

for tc in range(1, 11):
    N = int(input())
    obj = input()
    print('#{} {}'.format(tc, *plus(N, obj)))
