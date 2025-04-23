import heapq  ## 시간복잡도 (logn)
import sys
input = sys.stdin.readline

heap = []

n = int(input())
commands = [-int(input()) for _ in range(n)]

for command in commands:
  if command == 0:
    print( 0 if len(heap) == 0 else -heapq.heappop(heap))
  else:
    heapq.heappush(heap, command)
    
## heapq는 기본적으로 최소힙 지원
## heappop은 최소값을 pop하므로 최대힙을 구현하려면 음수로 값을 넣고 출력시 부호를 변환한다.