import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    word = list(input().rstrip())
    if word[0] != 'A' and word[0] != 'B' and word[0] != 'C' and word[0] != 'D' and word[0] != 'E' and word[0] != 'F':
        print('Good')
        continue
    chk = False
    prv = ''
    for i in range(1,len(word)-1):
        if i == 1:
            if word[i] == 'A' or (word[0] == 'A' and word[i] == 'F'):
                chk = True
                prv = word[i]
            else:
                chk = False
                break
        if i > 1:
            if prv == 'A' and (word[i] == 'A' or word[i] == 'F'):
                chk = True
                prv = word[i]
            elif prv == 'F' and (word[i] == 'F' or word[i] == 'C'):
                chk = True
                prv = word[i]
            else:
                chk = False
                break
    if word[-1] != 'A' and word[-1] != 'B' and word[-1] != 'C' and word[-1] != 'D' and word[-1] != 'E' and word[-1] != 'F':
        print('Good')
        continue
    if chk == True:
        print('Infected!')
    else:
        print('Good')