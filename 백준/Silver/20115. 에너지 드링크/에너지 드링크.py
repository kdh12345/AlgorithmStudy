import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse=True)

ans = 0
for i in range(len(arr)-1):
    ans = arr[i] + arr[i + 1] / 2
    arr[i+1] = ans

if ans == int(ans):
    print(int(ans))
else:
    print(ans)