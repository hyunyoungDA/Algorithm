
#소수인지를 확인할 때, 주어진 수 x를 2부터 x의 제곱근까지의 수로 나누어보고, 나누어떨어지는 수가 있는지를 확인해야 합니다
def is_prime(x):
    if x < 2:  # 0과 1은 소수가 아님
        return False
    for i in range(2, int(x ** 0.5) + 1):  # x의 제곱근까지만 확인
        if x % i == 0:
            return False  # x가 i로 나누어 떨어지면 소수가 아님
    return True

n = int(input())
count = 0

digit = list(map(int, input().split()))

for i in range(n):
    if is_prime(digit[i]):
        count += 1
    else:
        continue
print(count)