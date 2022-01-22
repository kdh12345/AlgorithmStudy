# 위상 정렬
#위상 정렬을 수행하면서 찾은 테크트리 순서대로, 해당 건물을 짓기까지 가장 오래 걸린 시간을 기록해 나갔고, 최종적으로 건물 W를 짓는데 걸린 시간을 구해 문제를 해결했습니다.
import sys
from collections import deque
def topologicalSort():
    for _ in range(n):
        if not dq:
            return
        target=dq.popleft()
        for x in adjList[target]:
            seq[x]=max(seq[x],seq[target]+d[x])
            indegree[x]-=1
            if not indegree[x]:
                dq.append(x)
t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    n,k=map(int,sys.stdin.readline().split())
    d=[0]+list(map(int,sys.stdin.readline().split()))

    seq=[0]*(n+1)
    indegree=[0]*(n+1)
    adjList=[[] for _ in range(n+1)]

    for _ in range(k):
        x,y=map(int,sys.stdin.readline().split())
        indegree[y]+=1
        adjList[x].append(y)
    w=int(sys.stdin.readline().rstrip())
    dq=deque()
    for i in range(1,n+1):
        if not indegree[i]: # 출발점 x기록
            seq[i]=d[i]
            dq.append(i)
    topologicalSort()
    print(seq[w])
