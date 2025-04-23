n = int(input())

values = list(map(int, input().split()))

values = sorted(set(values))

for value in values:
    print(value, end = " ")