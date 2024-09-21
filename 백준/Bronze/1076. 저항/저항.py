import sys
input = sys.stdin.readline

color1 = input().rstrip()
color2 = input().rstrip()
color3 = input().rstrip()

dic = {'black':0,'brown':1,'red':2,'orange':3,'yellow':4
       ,'green':5,'blue':6,'violet':7,'grey':8,'white':9}

dic2 = {'black':1,'brown':10,'red':100,'orange':1000,'yellow':10000
       ,'green':100000,'blue':1000000,'violet':10000000,'grey':100000000,'white':1000000000}

res1 = dic[color1]
res2 = dic[color2]

res = str(res1)+str(res2)
res = int(res)

res3 = dic2[color3]

ans = res * res3
print(ans)