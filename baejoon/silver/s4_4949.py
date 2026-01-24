import sys
input = sys.stdin.readline

res = []

while True:
    is_valid = True
    seq = input().rstrip()
    stack = []
    if seq == ".": break
    
    for s in seq:
        if s == "(" or s == "[":
            stack.append(s)
            
        elif s == ")":
             if len(stack) == 0:
                 is_valid = False
                 break 
             else:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    is_valid = False
                    break 
                
        elif s == "]":
            if len(stack) == 0:
                 is_valid = False
                 break 
            else:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    is_valid = False 
                    break 
        else: pass
        
    if is_valid and len(stack) == 0:
        res.append("yes")
    else:
        res.append("no")
    
for i in res:
    print(i)

    
    
    
