import sys

n = int(sys.stdin.readline().rstrip())
d_dic = {'ChongChong'}
for _ in range(n):
    a,b= sys.stdin.readline().split()
    if a in d_dic:
        d_dic.add(b)
    if b in d_dic:
        d_dic.add(a)

ans =len(d_dic)
print(ans)