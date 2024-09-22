import sys
input = sys.stdin.readline

n = int(input())
num_arr = list(map(int,input().split()))

index = [0]*(n+1)

for i in range(n):
    idx = num_arr[i]
    index[idx] = index[idx-1]+1

ans = n - max(index)
print(ans)