f = []
for _ in range(10):
    number = int(input())
    f.append(number)
f.sort(reverse=True)
s = []
for _ in range(10):
    number = int(input())
    s.append(number)
s.sort(reverse=True)

score1 = f[0]+f[1]+f[2]
score2 = s[0]+s[1]+s[2]
print(score1,score2)