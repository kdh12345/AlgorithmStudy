t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    sum_arr = [arr[0]]
    for i in range(1,len(arr)):
        big = max(sum_arr[i-1]+arr[i],arr[i])
        sum_arr.append(big)
    ans = max(sum_arr)
    print(ans)