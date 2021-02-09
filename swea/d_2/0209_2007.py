# 패턴 마디의 길이

T = int(input())
for t in range(1, T+1):
    words = input()
    N = len(words)
    # len_repeat_word = 0
    # 없어도 되는구나
    for i in range(1, N):
        if words[0] == words[i]:
            if words[0:i-1] == words[i: 2*i - 1]:
                len_repeat_word = i
                break
    print('#%d %d'%(t, len_repeat_word))
