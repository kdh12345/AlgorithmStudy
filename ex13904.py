import sys
import heapq

n = int(sys.stdin.readline().rstrip())
reports = []
ans = [0] * 1001

for _ in range(n):
    day, val = map(int,sys.stdin.readline().split())
    reports.append([-val,day,val])

heapq.heapify(reports) #heap으로 만들기

while reports:
    tmp = heapq.heappop(reports)
    for i in range(tmp[1],0,-1): # 마감일 뒤에서 부터
        if ans[i] == 0:
            ans[i] = tmp[2] # 점수
            break

answer = sum(ans)
print(answer)