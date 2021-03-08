# 4751. 다솔이의 다이아몬드 장식

T = int(input())
for t in range(1, T+1):
    deco = input()
    arr =['','','','','']
    i = 0
    for j in range(0, 4 * len(deco), 4):
        arr[0] += '..#.'
        arr[1] += '.#.#'
        arr[2] += '#.%s.'%deco[i]
        i += 1
        arr[3] += '.#.#'
        arr[4] += '..#.'

    arr[0] += '.'
    arr[1] += '.'
    arr[2] += '#'
    arr[3] += '.'
    arr[4] += '.'
    for i in arr:
        print(i)