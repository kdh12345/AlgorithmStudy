import sys
input = sys.stdin.readline

def su(r):
    sigyesu = list(map(int,str(r)))
    rot = [0,1,2,3]*4
    for i in range(4):
        new_num = int(sigyesu[rot[i+1]] * 1000
                      +sigyesu[rot[i+2]] * 100
                      +sigyesu[rot[i+3]] * 10
                      +sigyesu[rot[i]])
        if new_num < r:
            r = new_num
    return r

numbers = int(''.join(input().split()))

result = su(numbers)
ans = 0
for i in range(1111,result+1):
    chk = list(map(int,str(i)))

    if 0 not in chk:
        if su(i) == i:
            ans+=1
print(ans)