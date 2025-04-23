n = int(input())

def reverse_word(string):
    for i in range(len(string)):
        string[i] = string[i][::-1]
    return string
result = []
for _ in range(n):
    a = input().split()
    result.append(reverse_word(a))

for word in result:
    print(" ".join(word))
    