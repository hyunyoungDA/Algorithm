## 그래프 자료구조의 기본 문제
## bfs로 이웃한 모든 노드에게 바이러스를 적용하면 되는 문제
from collections import deque

n = int(input()) # 컴퓨터 개수
v = int(input()) # 연결선 개수

graph = [[] for i in range(n + 1)] # 그래프 초기화
visited = [0] * (n + 1) # 방문한 컴퓨터인지 표시

# 양방향 그래프이므로 두 노드에 모두 추가해줘야됨
for i in range(v): # 그래프 생성
    a,b = map(int,input().split())
    graph[a] += [b] # a에 b 연결
    graph[b] += [a] # b에 a 연결 -> 양방향
    
visited[1] = 1 # 1번 컴퓨터부터 시작

# 덱 사용 -> 시간복잡도가 Python 리스트에 비해 작음
# 임의 접근, 즉 인덱싱은 리스트가 더 빠름 
queue = deque([1])

while queue:
    e = queue.popleft()
    
    for neighbor in graph[e]:
        if visited[neighbor] == 0:
            queue.append(neighbor)
            visited[neighbor] = 1

# 1번 컴퓨터를 제외한 바이러스에 걸린 다른 컴퓨터의 수
print(sum(visited) - 1)