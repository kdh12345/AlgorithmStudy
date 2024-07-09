n = int(input())
str = input().rstrip()

rData = [v for v in str.split('B') if v]
bData = [v for v in str.split('R') if v]

ans = min(len(rData)+1,len(bData)+1)
print(ans)