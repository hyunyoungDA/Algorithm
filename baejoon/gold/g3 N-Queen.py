N = int(input()) # n * n 판의 크기 

# 퀸 N개를 서로 공격할 수 없게 놓는 문제 -> N이 주어졌을 때 퀸을 놓는 모든 방법

board = [[0 for _ in range(N)] for _ in range(N)]
cnt = 0

## map_[i][j]가 가능한 경우인지 판단하는 함수 
def is_threatening(row, col):
    for k in range(N):
        # Queen이 같은 행, 같은 열에 있는지 판단 
        if board[row][k] == 1 or board[k][col] == 1:
            return True
        
    for k in range(N):
        for l in range(N):
            # 대각성 상에 있는지 판단 
            if (k + l == row + col) or (k - 1 == row - col):
                if board[k][l] == 1:
                    return True
    return False

def queen(i):
    global cnt
    # N개의 퀸을 모두 놓았다면
    if i == N:
        cnt += 1
        return 
    for j in range(N):
        if (not(is_threatening(i,j))) and (board[i][j] != 1):
            board[i][j] = 1 # 이동한 것으로 업데이트
            if queen(i + 1):
                return True
            board[i][j] = 0 # 다음 여왕 말 배치 실패시 리셋
    return False

queen(0)

print(cnt)