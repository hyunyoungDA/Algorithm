r, value = map(int, input().split())


def is_prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

for i in range(r, value + 1):
    if is_prime(i):
        print(i)
        
## 소수 판별 -> 위 코드 시간 초과

r, value = map(int, input().split())

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):  # 2부터 제곱근까지의 수 중에서만 확인
        if x % i == 0:
            return False
    return True

for i in range(r, value + 1):
    if is_prime(i):
        print(i)


