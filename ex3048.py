import sys
n1 , n2=map(int,sys.stdin.readline().split())
g1 = [{'group':1,'name':ant} for ant in input()][::-1]
g2 = [{'group':2,'name':ant} for ant in input()]
ants = g1 + g2
t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    i = 0
    while i < len(ants) - 1:
        if ants[i]['group'] < ants[i+1]['group']:
            ants[i],ants[i+1] = ants[i+1],ants[i]
            i += 1
        i+=1

answer = ''.join([ant['name'] for ant in ants])
print(answer)