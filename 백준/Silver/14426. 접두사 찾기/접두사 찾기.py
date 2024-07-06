import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = []
for _ in range(n):
    arr.append(input().rstrip())

arr.sort()
ans = 0
s =[]
for i in range(m):
    test = input().rstrip()
    s.append(test)

s.sort()
i = 0
j = 0
while i<n and j<m:
    if arr[i][:len(s[j])] == s[j]:
        ans += 1
        j += 1
    elif arr[i] > s[j]:
        j+=1
    elif arr[i] < s[j]:
        i+=1
print(ans)