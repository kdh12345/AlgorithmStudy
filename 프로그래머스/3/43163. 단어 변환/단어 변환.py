answer = int(1e9)
visit=[0]*51
def chk(a,b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff+=1
    if diff == 1:
        return True
    else:
        return False
def dfs(b,t,cnt,words):
    global visit
    global answer
    for i in range(len(words)):
        if chk(b,words[i]) == True:
            if words[i] == t:
                answer = min(answer,cnt+1)
                return
            if visit[i] == 0:
                visit[i] = 1
                dfs(words[i],t,cnt+1,words)
                visit[i] = 0
    
def solution(begin, target, words):
    dfs(begin,target,0,words)
    if answer == int(1e9):
        return 0
    return answer