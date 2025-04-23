# 세준이 점수 -> max고름
# 모든 점수를 점수 / max * 100

n, m = list(map(int, input().split()))

numbers = list(map(int, input().split()))
sum_list = [0]
sum = 0
for i in numbers:
  sum += i
  sum_list.append(sum)

result = []
for i in range(m):
  i,j = list(map(int, input().split()))

  result.append(sum_list[j] - sum_list[i-1] )
  #print(sum_list[j] = sum_list[i-1])
  
for i in result:
  print(i)