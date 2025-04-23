n = int(input())
k = int(input())
results = []

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

for i in range(n,k+1):
    if is_prime(i):
        results.append(i)

if not results:
    print(-1)
else:
    result_min = min(results)
    result_sum = sum(results)
    print(result_sum)
    print(result_min)


