import sys
input = sys.stdin.readline

while True:

    try:
        s,t = map(str,input().split())

        chk = False
        idx = 0
        for i in range(len(t)):
            if s[idx] == t[i]:
                idx+=1
            if idx == len(s):
                chk = True
                break
        if chk == True:
            print('Yes')
        else:
            print('No')
    except:
        break
