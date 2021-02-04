#  지그재그 숫자

t = int(input())

for i in range(t):
    total = 0
    nums = int(input())
    for num in range(1, nums+1):
        if int(num) % 2:
            total += int(num)
        else:
            total -= int(num)
    print(f"#{i+1} {total}")

