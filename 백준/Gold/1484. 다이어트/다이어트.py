G = int(input())


y = 1
x = 2

res = []
while True:
    if x*x - (x-1)*(x-1) > 100000:
        break
    if x*x - y*y < G:
        x+=1
    elif x*x - y*y > G:
        y+=1
    elif x*x-y*y == G:
        res.append(x)
        x+=1

if len(res) >0:
    for ans in res:
        print(ans)
else:
    print(-1)
