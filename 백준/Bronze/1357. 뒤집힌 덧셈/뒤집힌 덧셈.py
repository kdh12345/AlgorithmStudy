import sys

x,y = map(int,sys.stdin.readline().split())

x=list(str(x))
y=list(str(y))
x.reverse()
y.reverse()

x=''.join(x)
y=''.join(y)
total = int(x)+int(y)
total=list(str(total))
total.reverse()
ans = ''.join(total)
print(int(ans))