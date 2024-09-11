import sys
input = sys.stdin.readline

n,k=map(int,input().split())
arr = [0]+list(map(int,input().split()))

ans = (-101)*n
total_arr=[0]*(n+1)
r_total =0

for i in range(1,n+1):
    total_arr[i] = total_arr[i-1]+arr[i]

for i in range(k,n+1):
    r_total = total_arr[i]-total_arr[i-k]
    ans = max(ans,r_total)

print(ans)