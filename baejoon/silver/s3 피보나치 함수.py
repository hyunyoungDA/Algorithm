memo = {} #메모이제이션: 이미 계산된 값이 있으면 캐시에서 반환

def fib(x):
    if x in memo:
        return memo[x]
    if x == 0:
        result = (1,0)
    elif x == 1:
        result = (0,1)
    else:
        # 재귀 호출하여 피보나치 수 계산
        count1 = fib(x - 1)
        count2 = fib(x - 2)
        result = (count1[0] + count2[0], count1[1] + count2[1])  # (0의 개수, 1의 개수)
    
    # 계산 결과를 캐시에 저장
    memo[x] = result
    
    return result

n = int(input())
values = []

for _ in range(n):
    a = int(input())
    values.append(fib(a))

# count_0 ,count_1로 언패킹
for count_0, count_1 in values:
    print(f"{count_0} {count_1}")