def comb(x,y):
    if y > x or x < 0 or y < 0:
        return 0
    if y == 0 or y == x:
        return 1
    if y > x - y:
        y = x - y
    numerator = 1  #분자
    denominator = 1 #분모
    
    for i in range(y):
        numerator *= x - i
        denominator *= i + 1
    return numerator // denominator
        
        
        
        
a,b = map(int, input().split())

result = comb(a,b)
print(result)
