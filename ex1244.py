import sys
n=int(sys.stdin.readline().rstrip())
arr = [-1]+list(map(int,sys.stdin.readline().split()))
stu_cnt = int(sys.stdin.readline().rstrip())
for i in range(stu_cnt):
    sex,cnt = map(int,sys.stdin.readline().split())
    if sex == 1:
        for i in range(cnt,n+1,cnt):
            if arr[i] == 0:
                arr[i] = 1
            elif arr[i] == 1:
                arr[i] = 0
    elif sex == 2:
        if arr[cnt] == 0:
            arr[cnt] = 1
        elif arr[cnt] == 1:
            arr[cnt] = 0
        for j in range(n//2):
            if cnt+j > n or cnt-j < 1:
                break
            if arr[cnt-j] == arr[cnt+j]: #좌우대칭
                if arr[cnt-j] == 0:
                    arr[cnt-j] = 1
                elif arr[cnt-j] == 1:
                    arr[cnt-j] = 0
                if arr[cnt+j] == 0:
                    arr[cnt+j] = 1
                elif arr[cnt+j] == 1:
                    arr[cnt+j] = 0
            else:
                break

for i in range(1,n+1):
    print(arr[i],end= ' ')
    if i % 20 == 0:
        print()
