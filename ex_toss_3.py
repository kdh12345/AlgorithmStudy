import sys
k = 80
dungeons = [ [80,20], [50,40], [30,10] ]
dungeons.sort(key= lambda x:(-x[0],x[1]))
arr = dungeons[1:]

for i in range(len(arr)-1):
    if arr[i][0] > arr[i+1][0] and arr[i][1] > arr[i+1][1]:
        arr[i][0], arr[i+1][0] = arr[i+1][0], arr[i][0]
        arr[i][1], arr[i + 1][1] = arr[i + 1][1], arr[i][1]

new_arr = dungeons[:1] + arr

ans = 0
for item in new_arr:
    demand = item[0]
    use = item[1]
    if k >= demand:
        k -= use
        ans+=1
print(ans)
