def is_empty(stack):
    if len(stack) == 0:
        return False
    else:
        return True

def stack_check(num_list):
    stack = []
    answer = []  # 기호 저장 
    current = 1
    possible = True
    
    for num in num_list:
        while current <= num:
            stack.append(current)
            answer.append("+")
            current += 1
        if is_empty(stack) and stack[-1] == num: #stack이 비어있는지 확인 
            stack.pop()
            answer.append("-")
        else:
            possible = False
            break
    if possible:  #조건문 -> 변수 자체로 가능, 현재 True이므로 answer가 출력됨
        return answer
    else:
        return ["NO"]
            

n = int(input())

num_list = [int(input()) for i in range(n)]

results = stack_check(num_list)

for result in results:
    print(result)


