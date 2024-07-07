m,n = map(int,input().split())
stores = []
for _ in range(int(input())+1):
    dir,dist = map(int,input().split())
    pos = -1
    if dir == 1:
        pos = m-dist
    if dir == 2:
        pos = n+m+dist
    if dir == 3:
        pos = m+dist
    if dir == 4:
        pos = 2*(n+m)-dist

    stores.append(pos)

my_pos = stores.pop()
ans = 0
for store_pos in stores:
    dist1 = abs(store_pos-my_pos)
    dist2 = n*2+m*2-dist1
    ans += min(dist1,dist2)
print(ans)