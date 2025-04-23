## x가 자연수라면 배열에 추가. 0이라면 가장 작은 값 출력 및 제거

import heapq  ## 시간복잡도 (logn)
import sys
input = sys.stdin.readline

heap = []

n = int(input())
commands = [int(input()) for _ in range(n)]

for command in commands:
  if command == 0:
    print( 0 if len(heap) == 0 else heapq.heappop(heap))
  else:
    heapq.heappush(heap, command)


# heap = []

# n = int(input())  #입력 횟수
# commands = [int(input()) for i in range(n)]  #입력값

# for command in commands:
#   if command == 0:
#     if len(heap) == 0:
#       print(0)
#     else:
#       if heap:
#         min_idx = heap.index(min(heap))
#         print(min(heap))
#         heap.pop(min_idx)
#       else:
#         pass
      
#   else:
#     heap.append(command)
    
    


