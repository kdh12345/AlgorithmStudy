import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
word = list(sys.stdin.readline().rstrip())

p = 'IOI'
for i in range(2,n+1):
    p += 'OI'

l = len(p)
ans = 0
for i in range(len(word)):
    if ''.join(word[i:i+l]) == p:
        ans += 1
        i = i+n
        
print(ans)
