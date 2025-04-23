# import sys
# input = sys.stdin.readline

# n = int(input())


# lectures = [tuple(map(int, input().split())) for _ in range(n)]

# # 종료 시간을 기준으로 정렬 -> 1개의 프로세서에서 들어갈 수 있는 최대의 회의 
# lectures.sort(key = lambda x: x[1])

# # 정렬한 후 종료시간이 가장 빠른 lectures[0]을 초깃값으로 
# solution = [lectures[0]]
# i = 0
# for j in range(1, len(lectures)):
#     if lectures[j][0] >= lectures[i][1]:  # 직전에 선택된 동아리의 종료시간 이후에 시작하면
#         solution.append(lectures[j])
#         i = j

# print(len(solution))


import sys
input = sys.stdin.readline

n = int(input())

lectures = [tuple(map(int, input().split())) for _ in range(n)]

# 종료시간 기준, 같으면 시작시간 기준으로 정렬 -> 이 조건을 추가해줘야됨
lectures.sort(key=lambda x: (x[1], x[0]))

count = 1  # 첫 회의 선택
last_end = lectures[0][1]

for i in range(1, n):
    start, end = lectures[i]
    if start >= last_end:
        count += 1
        last_end = end

print(count)
