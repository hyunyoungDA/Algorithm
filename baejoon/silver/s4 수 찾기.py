results = []

q = int(input())
q_num = set(map(int , input().split()))  #set은 해시 테이블 사용 -> 시간복잡도 O(1)

a = int(input())
a_num = list(map(int, input().split()))

for i in range(a):
    if a_num[i] in q_num:
        results.append(1)
    else:
        results.append(0)

for result in results:
    print(result)