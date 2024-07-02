n = int(input())
s = input()

couple = s.count('LL')

if couple <= 1:
    print(n)
else:
    ans = n+1-couple
    print(ans)