import sys
input = sys.stdin.readline

n = int(input())
A = []   # 10,1,5,2,3

for i in range(n):
  A.append((int(input()), i)) # 인덱스도 함께 저장
  
_max = 0
sorted_A = sorted(A)  # 1,2,3,5,10

for i in range(n):
  if _max < sorted_A[i][1] - i:  
    # 현재 sorted_A에 원래 인덱스가 3인 값 2가 인덱스 1에 저장되어있음
    # i는 기본 인덱스이므로 sorted_A[1][1] - i는 원래 인덱스가 3이였던 값 2가 왼쪽으로 두 번 이동한 것.
    # sorted_A[1][1] = 3이고 i = 1이므로 _max = 2, 즉 왼쪽으로 2번 이동한것임. 
    _max = sorted_A[i][1] - i
    
print(_max + 1)
  