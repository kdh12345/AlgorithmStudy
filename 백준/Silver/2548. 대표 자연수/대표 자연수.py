import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

if len(arr) % 2 == 0:
    ans = arr[len(arr)//2-1]
    print(ans)
else:
    ans = arr[len(arr) // 2]
    print(ans)
