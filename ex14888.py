import sys
max_val=-int(1e9)
min_val=int(1e9)
def make_num(arr,now,idx,pl,mi,mu,div):
    global max_val,min_val
    if idx==len(arr):
        max_val=max(max_val,now)
        min_val=min(min_val,now)
        return
    if pl>0:
        make_num(arr, now+arr[idx], idx+1, pl-1, mi, mu, div)
    if mi>0:
        make_num(arr, now - arr[idx], idx + 1, pl, mi-1, mu, div)
    if mu>0:
        make_num(arr, now * arr[idx], idx + 1, pl, mi, mu-1, div)
    if div>0:
        make_num(arr, int(now / arr[idx]), idx + 1, pl, mi, mu, div-1)
n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().split()))
op=list(map(int,sys.stdin.readline().split()))
pl=op[0]
mi=op[1]
mu=op[2]
div=op[3]
make_num(arr,arr[0],1,pl,mi,mu,div)
print(max_val)
print(min_val)