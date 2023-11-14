import sys
s = list(sys.stdin.readline().strip())
ans = ''
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        if len(ans) < 3:
            ans += s[i-1] + s[i]
print(ans[:-1])