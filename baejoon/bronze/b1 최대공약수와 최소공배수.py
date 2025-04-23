import math

def gcd(x,y):
    return math.gcd(x,y)

def lcm(x,y):
    return (x*y) // gcd(x,y)

a,b = map(int, input().split())

print(gcd(a,b))
print(lcm(a,b))