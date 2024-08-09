import sys
input = sys.stdin.readline

n,q = map(int,input().split())
numbers = list(map(int,input().split()))
numbers.sort()

total = [0]
for i in range(n):
    total.append(numbers[i]+total[i])

for i in range(q):
    s,e = map(int,input().split())
    ans = total[e] - total[s-1]
    print(ans)