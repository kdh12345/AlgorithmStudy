import sys
n,w,l=map(int,sys.stdin.readline().split())
truck=list(map(int,sys.stdin.readline().split()))
t=[]
weight=0
ans=0
for item in truck:
    while True:
        if len(t)==0:
            t.append(item)
            weight+=item
            ans+=1
            break
        elif len(t)<w:
            if weight+item<=l:
                t.append(item)
                weight+=item
                ans+=1
                break
            else:
                t.append(0)
                ans+=1
        if len(t)==w:
            weight-=t[0]
            t.pop(0)
ans+=w
print(ans)
