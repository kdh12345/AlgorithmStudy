import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    word = input().rstrip()
    arr.append(word)

arr.sort(key=len)

ans = 0
for i in range(n):
    chk = False
    for j in range(i+1,n):
        if arr[i] == arr[j][:len(arr[i])]:
            chk = True
            break
    if chk == False:
        ans+=1

print(ans)