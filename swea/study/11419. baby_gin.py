# 11419. baby_gin
def baby_gin(cards):
    for i in range(len(cards)):
        count_cards[cards[i]] += 1
    i = 0
    run = 0
    triplet = 0
    while i < 10:
        if count_cards[i] >= 3:
            run += 1
            count_cards[i] -= 3
            continue
        elif count_cards[i] >= 1 and count_cards[i+1] >= 1 and count_cards[i+2] >= 1:
            triplet += 1
            count_cards[i] -= 1
            count_cards[i+1] -= 1
            count_cards[i+2] -= 1
            continue
        i += 1
    result = run + triplet
    return result

# counting 을 활용한 방법이 있구나....
T = int(input())
for t in range(1, T+1):
    cards = list(map(int, input()))
    count_cards = [0] * 12
    result = baby_gin(cards)
    ans = 'Lose'
    if result == 2:
        ans = 'Baby Gin'
    print('#%d %s'%(t, ans))