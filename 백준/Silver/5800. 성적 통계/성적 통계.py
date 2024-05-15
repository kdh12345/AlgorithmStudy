import sys

k = int(sys.stdin.readline().rstrip())

for i in range(k):
    arr = list(map(int,sys.stdin.readline().split()))
    arr = arr[1:]
    max_val = max(arr)
    min_val = min(arr)
    arr = sorted(arr,reverse=True)
    gap = []
    for j in range(len(arr)-1):
        diff = arr[j]-arr[j+1]
        gap.append(diff)
    l_gap = max(gap)
    print('Class '+str(i+1))
    print('Max '+str(max_val)+', '+'Min '+str(min_val)+', '+'Largest gap '+str(l_gap))
