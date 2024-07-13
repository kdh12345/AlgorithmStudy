t = int(input())

for _ in range(t):
    ans = 987654321
    n = int(input())
    arr = list(map(str,input().split()))
    if n > 32:
        print(0)
    else:
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    total = 0
                    if i == j or j == k or i == k:
                        continue
                    for p in range(4):
                        if arr[i][p] != arr[j][p]:
                            total+=1
                        if arr[j][p] != arr[k][p]:
                            total+=1
                        if arr[i][p] != arr[k][p]:
                            total+=1
                    ans = min(ans,total)
        print(ans)