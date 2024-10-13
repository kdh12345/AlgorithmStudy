

def dfs(n,computers,idx,visit):
    visit[idx] = 1
    for i in range(n):
        if i != idx and computers[idx][i] == 1:
            if visit[i] == 0:
                dfs(n,computers,i,visit)
        
def solution(n, computers):
    answer = 0
    visit=[0 for _ in range(n)]
    
    for i in range(n):
        if visit[i] == 0:
            dfs(n,computers,i,visit)
            answer+=1
    return answer