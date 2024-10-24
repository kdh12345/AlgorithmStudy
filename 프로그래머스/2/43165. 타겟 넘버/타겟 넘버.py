answer = 0
def dfs(arr,target,start,idx,plus,minus):
    global answer
    if idx == len(arr):
        if start == target:
            answer += 1
        return
    if plus > 0:
        dfs(arr,target,start+arr[idx],idx+1,plus-1,minus)
    if minus > 0:
        dfs(arr,target,start-arr[idx],idx+1,plus,minus-1)
def solution(numbers, target):
    dfs(numbers,target,0,0,len(numbers),len(numbers))
    return answer