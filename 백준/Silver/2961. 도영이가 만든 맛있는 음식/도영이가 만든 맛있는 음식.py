from itertools import combinations

n = int(input())
a_sum = []
b_sum = []
a_candi = []
b_candi = []

for _ in range(n):
    a,b = map(int,input().split())
    if n == 1:
        print(abs(a-b))
        exit(0)
    else:
        a_sum.append(a)
        b_sum.append(b)

# sin
for i in range(1,n+1):
    for a_item in combinations(a_sum,i):
        num = 1
        for j in a_item:
            num *= j
        a_candi.append(num)

    for b_item in combinations(b_sum,i):
        num2 = sum(b_item)
        b_candi.append(num2)

result = []
for i in range(len(a_candi)):
    result.append(abs(a_candi[i] - b_candi[i]))

ans = min(result)
print(ans)