import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort(reverse=True)
totalTime = [0]*m # 전자기기 시간 총 합

idx = 0
for i in range(len(arr)):
    if idx == 0:
        totalTime[idx] += arr[i]
        idx = (idx+1) % m
        continue

    totalTime[idx] += arr[i]
    if totalTime[idx-1] == totalTime[idx]:
        idx = (idx+1) % m

print(totalTime[0])