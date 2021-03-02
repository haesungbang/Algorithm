# 11579. 반복문자 지우기

T = int(input())
for t in range(1, T+1):
    words = list(map(str, input()))
    result = []
    for i in range(len(words)):
        if len(result) == 0:
            result.append(words[i])
        else:
            if words[i] != result[-1]:
                result.append(words[i])
            else:
                result.pop()
    print('#%d %d'%(t, len(result)))