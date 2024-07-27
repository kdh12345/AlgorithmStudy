import sys
input = sys.stdin.readline

n,k = list(map(int,input().rstrip().split()))
dolls = list(map(int,input().rstrip().split()))

s = 0
e = k
cnt = dolls[s:e+1].count(1)

result = 987654321

while e < n:
    if cnt == k:
        result = min(result,e-s+1)
        if dolls[s] == 1:
            cnt -= 1
        s += 1
    elif cnt < k:
        e += 1
        if e < n and dolls[e] == 1:
            cnt += 1
    else:
        if dolls[s] == 1:
            cnt -= 1
        s += 1

if result == 987654321:
    print(-1)
else:
    print(result)