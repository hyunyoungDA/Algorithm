memo = {} #메모이제이션 -> 캐시에 저장해서 중복된 계산 피할 수 있음
def fib(x):
    if x in memo:
        return memo[x]
    elif x == 0:
        result = 0
    elif x == 1:
        result = 1
    else:
        result = fib(x-1) + fib(x-2)
    memo[x] = result
    return result

n = int(input())

result = fib(n)
print(result)