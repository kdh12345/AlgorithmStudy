# n번째 큰 수
import sys
t = int(sys.stdin.readline().rstrip()) # test case
for _ in range(t):
    arr = list(map(int,sys.stdin.readline().split()))
    arr.sort()
    print(arr[-3])
