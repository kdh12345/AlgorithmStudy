import sys
n,m = map(int,sys.stdin.readline().split())
rank_arr = [sys.stdin.readline().split() for _ in range(n)]

def bs(rank, cnt):
    s = 0
    e = len(rank) - 1
    ans = 0
    while s <= e:
        mid = (s+e) // 2
        if int(rank_arr[mid][1]) >= cnt: #상한선 체크
            e = mid - 1
            ans = mid
        else:
            s = mid + 1
    return ans

for i in range(m):
    cnt = int(sys.stdin.readline())
    print(rank_arr[bs(rank_arr,cnt)][0])
