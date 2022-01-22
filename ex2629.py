import sys
def get_scale(chu_weight,chu,now,left,right,candi):
    new=abs(right-left)
    if new not in candi:
        candi.append(new)
    if now==chu:
        return 0
    if dp[now][new]==0:
        # left
        get_scale(chu_weight,chu,now+1,left+chu_weight[now],right,candi)
        # right
        get_scale(chu_weight, chu, now + 1, left, right+ chu_weight[now], candi)
        # nothing
        get_scale(chu_weight, chu, now + 1, left, right, candi)
        dp[now][new]=1
chu=int(sys.stdin.readline().rstrip())
chu_weight=list(map(int,sys.stdin.readline().split()))
chu_weight=sorted(chu_weight)
bead=int(sys.stdin.readline().rstrip())
bead_weight=list(map(int,sys.stdin.readline().split()))
dp=[[0]*15001 for _ in range(chu+1)]
candi=[]
get_scale(chu_weight,chu,0,0,0,candi)
for i in range(len(bead_weight)):
    if bead_weight[i] in candi:
        print('Y',end=' ')
    else:
        print('N',end=' ')