import sys
from collections import Counter
n=int(sys.stdin.readline().rstrip())
recommend=int(sys.stdin.readline().rstrip())
stu=list(map(int,sys.stdin.readline().split()))
pic=[]
score=[]
for i in range(recommend):
    if stu[i] in pic:
        for j in range(len(pic)):
            if stu[i]==pic[j]: # 어떤 학생이 특정 학생을 추천하면, 추천받은 학생의 사진이 반드시 사진틀에 게시되어야 한다.
                score[j]+=1
    else:
        if len(pic)>=n: #비어있는 사진틀이 없는 경우
            for j in range(n):
                if score[j]==min(score):
                    del score[j]
                    del pic[j]
                    break
        pic.append(stu[i])#현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가시킨다.
        score.append(0)#사진틀에 게시된 사진이 삭제되는 경우에는 해당 학생이 추천받은 횟수는 0으로 바뀐다.
pic.sort()
print(' '.join(map(str,pic)))



