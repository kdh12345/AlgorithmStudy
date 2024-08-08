n = int(input())
m = int(input())

h = m - n
one = 1
two = 1

for i in range(1,h+n):
    one*=i
for i in range(1,h+1):
    two*=i
for i in range(1,n):
    two*=i

ans = one//two
print(ans)