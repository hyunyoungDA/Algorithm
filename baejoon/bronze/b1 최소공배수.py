import math

results = []

def gcd(a,b):
    return math.gcd(a,b)

def lcm(a,b):
    return a * b // gcd(a,b)

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    
    gcd(x,y)
    results.append(lcm(x,y))
    
for result in results:
    print(result)  
## 유클리드 호제법으로 구한 최소 공배수, 최대 공약수
   
   
n = int(input())

for i in range(n):
    a,b = map(int, input().split())

    for i in range(max(a,b),(a*b)+1):
        if i % a == 0 and i % b == 0:
            print(i)
            break
