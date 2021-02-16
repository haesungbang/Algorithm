# 패턴 마디의 길이

T = int(input())
for t in range(1, T+1):
    words = input()
    N = len(words)
    # len_repeat_word = 0
    # 없어도 되는구나
    for i in range(1, N):
        # 가장 먼저 시작값이 같은 것을 찾는다.
        if words[0] == words[i]:
            # 시작값과 찾은 값 사이의 있는 길이의 단어가 같은지 확인한다.
            if words[0:i-1] == words[i: 2*i - 1]:
                len_repeat_word = i
                break
                # 반복되는 단어를 찾으면 반복문을 그만한다.
    print('#%d %d'%(t, len_repeat_word))
