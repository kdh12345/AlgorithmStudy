
ans = 0
idx = 0
for i in range(5):
    scores = list(map(int,input().split()))
    total = sum(scores)
    if ans < total:
        ans = total
        idx = i+1
print(idx,ans)