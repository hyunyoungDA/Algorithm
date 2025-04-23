n = int(input())

data = list(map(int, input().split())) # 3 1 4 3 2

data.sort()  # 정렬 1 2 3 3 4

cumulative_sum = []
current_sum = 0

for i in data:
    current_sum += i
    cumulative_sum.append(current_sum)

print(sum(cumulative_sum))

# current_sum = 1 / cumulative_sum = [1]
# current_sum = 3 / cumulative_sum = [1,3,6,9,13]