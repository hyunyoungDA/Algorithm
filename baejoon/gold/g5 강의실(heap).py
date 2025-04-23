import sys
import heapq

input = sys.stdin.readline
n = int(input())

lectures = [tuple(map(int, input().split())) for _ in range(n)]

# 최소한의 프로세서 개수 문제는 시작 시간을 기준으로 했을 때 최적해가 나옴
# 시작 시간을 기준으로 정렬
lectures.sort(key=lambda x: x[1])  # x[1]은 시작 시간

heap = []

# 가장 첫 강의의 종료 시간을 heap에 넣음
heapq.heappush(heap, lectures[0][2])  # x[2]는 종료 시간

for i in range(1, n):
    start = lectures[i][1]
    end = lectures[i][2]
    
    # 현재 강의의 시작 시간 >= 가장 빨리 끝나는 강의 시간 이면, 해당 강의실 재사용 가능
    if start >= heap[0]:
        heapq.heappop(heap)
    
    # 새 강의 종료 시간 push (기존 강의실이든 새 강의실이든)
    heapq.heappush(heap, end)

print(len(heap))  # heap에 남은 수가 최소 강의실 수
