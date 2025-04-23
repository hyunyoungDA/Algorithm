n, m = map(int, input().split())
res = []
origin_array = [[0] * (n+1)]  ## 1번 인덱스부터 처리해주기 위해, out of index해결
d = [[0] * (n + 1) for _ in range(n+1)] # 구간 합을 저장하기 위한 배열

for i in range(n):
  origin_array_row = [0] + [int(x) for x in input().split()] # 실제갑은 인덱스가 1부터.
  origin_array.append(origin_array_row)
  
for i in range(1, n + 1):
  for j in range(1, n + 1):
    d[i][j] = d[i][j-1] + d[i-1][j] - d[i-1][j-1] + origin_array[i][j]
    
for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  result = d[x2][y2] - d[x1-1][y2] - d[x2][y1 - 1] + d[x1 - 1][y1 - 1]
  res.append(result)
  
for i in res:
  print(i)
