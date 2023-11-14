import sys
n,m = map(int,sys.stdin.readline().split())
num_arr = list(map(int,sys.stdin.readline().split()))

# sum 구하기
sum_arr = [0]*(n+1)
tmp = 0
for i in range(n+1):
    tmp += num_arr[i-1]
    sum_arr[i] = tmp

#print()
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    print(sum_arr[b]-sum_arr[a-1])