import sys
n = int(sys.stdin.readline().rstrip())

points = []
maxH = 0
maxL = 0
maxIdx =0
for i in range(n):
    l, h = map(int,sys.stdin.readline().split())
    points.append([l,h])

    if maxL < l:
        maxL = l
    if maxH < h:
        maxH = h
        maxIdx = l


points.sort(key=lambda x:(x[0], x[1]))

area = 0
pillars = [0]*(maxL+1)

for l,h in points:
    pillars[l] = h

tmp = 0
for i in range(maxIdx+1): # left to mid
    if pillars[i] > tmp:
        tmp = pillars[i]
    area+=tmp

tmp = 0
for i in range(maxL,maxIdx,-1): # right to mid
    if pillars[i] > tmp:
        tmp = pillars[i]
    area+=tmp

print(area)