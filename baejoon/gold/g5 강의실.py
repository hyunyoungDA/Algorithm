# 분할정복, 그리디 스케쥴링?
# 입력: 강의 번호, 강의 시간, 강의 종료 시간
# 종료 시간 기준으로 정렬한 후 스케쥴링
# 시간 초과 
import sys

n = int(sys.stdin.readline())

values = []

for _ in range(n):
    values.append(list(map(int, sys.stdin.readline().split())))
    
values.sort(key = lambda x: x[2])

cnt = 0
solution = [[values[0]]]
finish_time = [values[0][2]]

for i in range(1, n):
    flag = False
    for j in range(cnt + 1):
        if values[i][1] >= finish_time[j]:
            solution[j].append(values[i])
            finish_time[j] = values[i][2]
            flag = True
            break
    if not flag:
        cnt += 1 # 미팅룸 하나 추가
        solution.append([values[i]])
        finish_time.append(values[i][2])
        
print(len(solution))
            

