import sys
import bisect
sys.setrecursionlimit(10**6)

N, M, R = list(map(int, sys.stdin.readline().split()))

# 인덱스를 1부터 사용, 빈 그래프 하나 생성 
graph = [[] for _ in range(N + 1)]

# 정점 u와 v를 입력 받고 정렬된 상태로 graph의 각 정점별로 추가
# 무방향, 양방향 그래프이므로 양쪽에 모두 추가해줘야됨 
for _ in range(M):
    u, v = list(map(int, sys.stdin.readline().split()))
    bisect.insort(graph[u],v)
    bisect.insort(graph[v],u)
    
visited = [False] * (N + 1)
order = [0] * (N + 1)
cnt = 1

def bfs(node):
    global cnt
    
    queue = []
    visited[node] = True
    queue.append(node)
    order[node] = cnt
    cnt += 1
    
    while queue:
        e = queue.pop(0)
        for neighbor in graph[e]:
            if not visited[neighbor]:
                visited[neighbor] = True
                order[neighbor] = cnt
                cnt += 1
                queue.append(neighbor)
                
bfs(R)

for i in range(1, N + 1):
    print(order[i])


    
    
    
