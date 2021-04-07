# 사전
# 사전을 만들고 사전에서 찾고자 하는 단어가 몇 번째 있는지 확인하시오.
def dic(word):
    global result
    vowels = ['A', 'E', 'I', 'O', 'U']
    result.append(word)
    if len(word) < 5:
        for i in range(5):
            k = word + vowels[i]
            dic(k)
    # return 이 없어도 되는구나?
def answer(result, match):
    for i in range(len(result)):
        if result[i] == match:
            return i
    return -1

vowels = ['A', 'E', 'I', 'O', 'U']
result = []
dic(vowels[0])
# print(result)
match = input()
ans = answer(result, match)
print(ans)