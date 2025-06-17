# 배낭에 가장 효율적으로 물건을 넣을 수 있는 방법 
N, K = map(int, input().split())
W = []
V = []

for _ in range(N):
    weight, value = map(int, input().split())
    W.append(weight)
    V.append(value)

# DP 테이블 생성 
T = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(N):
    # 배낭의 크기를 1씩 증가시키면서 동적 프로그래밍 
    for j in range(K+1):
        # 물품을 현재 배낭 용량에 담을 수 없을 경우 
        if W[i] > j:
            # 이전 물품까지 고려했을 때 얻을 수 있었던 최대 가지 그대로 갱신 
            T[i][j] = T[i-1][j] # 각 무게마다 가능한 경우와 불가능한 경우를 처리 
        # 현재 물품을 용량에 담을 수 있는 경우
        # 2가지 선택지를 모두 고려 
        else:
            T[i][j] = max(T[i-1][j], V[i] + T[i-1][j - W[i]]) # 두 가지 경우에 대해 최댓값으로 처리
            # V[i] + T[i-1][j-W[i]]는 현재 물품에 대한 가치를 얻고 남은 배냥 용량 계산
            # 그냥 이전 물품까지만 고려해서 채웠을 때 얻은 최대 가치에 새로운 Value 더해준 것 
            
print(T[N-1][j]) 