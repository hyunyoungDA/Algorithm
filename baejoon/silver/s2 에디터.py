## L : 커서 왼쪽으로 한칸(맨 앞이면 무시), D:커서를 오른쪽(맨 뒤면 무시)
## B: 커서 왼쪽에 있는 문자 삭제 p x: x라는 문자를 커서 왼쪽에 추가 

n = input()
m = int(input())

commands = [input().split() for _ in range(n)]

class editor():
  def __init__(self):
    self.line = []
    
    
  