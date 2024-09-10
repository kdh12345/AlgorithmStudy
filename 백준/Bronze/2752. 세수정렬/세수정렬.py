import sys
input = sys.stdin.readline

arr = list(map(int,input().split()))
arr.sort()

for item in arr:
    print(item,end=' ')