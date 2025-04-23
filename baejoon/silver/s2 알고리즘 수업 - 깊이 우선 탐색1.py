## N개의 정점과 M개의 간선으로 구성된 무방향 그래프, 모든 가중치는 1
## 백준에서 재귀 사용시 setrecursionlimit, 입력 속도 개선 sys.stdin.readline() 사용
import sys
import bisect # 이진 정렬 기법
sys.setrecursionlimit(10 ** 6) # 백준에서는 재귀 호출에 제한이 있으므로 제한 임의로 설정

N, M, R = list(map(int, sys.stdin.readline().split()))

# 인덱스를 1부터 사용하기 위해 N + 1
graph = [[] for _ in range(N + 1)]


## 무방향그래프이므로, u에서 v로 이동하거나 v에서 u로 이동할 수 있다.
## 그러므로 u,v정점을 받을 때 각 graph에 정점을 추가해준다.
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    
    ## 정렬이 된 상태로 삽입 가능 -> 따로 정렬해주지 않아도 되므로 시간 복잡도 개선 가능
    bisect.insort(graph[u], v)
    bisect.insort(graph[v], u)
    
# for adj in graph:
#     adj.sort()

## 정점의 개수만큼 visited 여부 확인, 인덱스를 1부터 사용하므로 N + 1
visited = [False] * (N + 1)
order = [0] * (N + 1) # 방문 순서 기록 리스트
cnt = 1
    
def dfs(node):
    global cnt
    visited[node] = True # 받은 node에 대해 visited = True
    order[node] = cnt # 해당 node에 대한 방문 순서 기록
    cnt += 1

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)

dfs(R)

for i in range(1, N + 1):
    print(order[i])