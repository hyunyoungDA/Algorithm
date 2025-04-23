# 점수 -> 문제를 풀기 시작한 시간부터 경과한 시간 + 난이도로 결정
# 풀이하지 못한 경우 0점
# 참가자의 총 점수는 가장 높은 점수 5개의 합
# 출력은 총합과 문제 번호(번호가 증가하는 순서)

values = []
exams = [0]

for _ in range(8):
    values.append(int(input()))
    
sorted_value = sorted(values) # 정렬하면 0 20 30 33 48 50 54 66

sum = 0
for value in sorted_value[3:]:
    sum += value
    exams.append(values.index(value) + 1)
    
exams.sort()
exams.pop(0)
    
print(sum)
for exam in exams:
    print(exam, end = " ")
    
##############################################3
## 개선된 코드

values = []

for i in range(8):
    score = int(input())
    values.append((score, i + 1)) # 점수와 문제 번호를 동시에 저장

values.sort()

# 가장 높은 점수 5개 선택
top_five = values[-5:]

# 총합 계산
total_score = sum(score for score, _ in top_five)

# 문제 번호 추출 및 정렬
problem_numbers = sorted(num for _, num in top_five)

# 출력
print(total_score)
print(*problem_numbers)