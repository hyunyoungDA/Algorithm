# X 좌표를 우선으로 오름차순 정렬
# 동일하다면 y 좌표가 오름차순 정렬
# 예를 들어서 점의 개수 N (1 <= N <= 100,000) 
# 현재 시간 제한이 1초이고, 메모리 제한은 256MByte
# Python 기준 1초에 약 2000만번 연산 
# O(n ^ 2)는 지금 안됨 -> 시간 제한 1초라서 

import sys 
input = sys.stdin.readline 

n = int(input())

xys = []

# O(N)
for _ in range(n):
    x_n_y = list(map(int, input().split()))
    xys.append(x_n_y) # [x, y]
    
xys = sorted(xys, key = lambda x: (x[1], x[0]))

for x,y in xys:
    print(x, y)


