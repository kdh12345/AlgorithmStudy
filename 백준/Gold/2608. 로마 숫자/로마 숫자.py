import sys
def arabia(word):
    answer = 0
    visit = [False]*len(word)

    for i in range(len(word)):
        if visit[i] == False:
            if len(word) > i+1 and word[i:i+2] in dic2:
                visit[i] = True
                visit[i+1] = True
                answer += dic2[word[i:i+2]]
            else:
                answer += dic[word[i]]
                visit[i] = True
    return answer

def roma(n):
    s = ''
    while n > 0:
        if n >= 1000:
            s+='M'
            n-=1000
        elif n>=900:
            s+='CM'
            n-=900
        elif n>=500:
            s+='D'
            n-=500
        elif n>=400:
            s+='CD'
            n-=400
        elif n>=100:
            s+='C'
            n-=100
        elif n>=90:
            s+='XC'
            n-=90
        elif n>=50:
            s+='L'
            n-=50
        elif n>=40:
            s+='XL'
            n-=40
        elif n>=10:
            s+='X'
            n-=10
        elif n>=9:
            s+='IX'
            n-=9
        elif n>=5:
            s+='V'
            n-=5
        elif n>=4:
            s+='IV'
            n-=4
        elif n>=1:
            s+='I'
            n-=1
    return s
word1 = str(sys.stdin.readline().rstrip())
word2 = str(sys.stdin.readline().rstrip())

dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
dic2 = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}


ans = arabia(word1)+arabia(word2)
print(ans)
print(roma(ans))
