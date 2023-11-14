from collections import deque
tasks = [1,1,2,3,3,2,2]
tasks.sort()
set_tasks = list(set(tasks))
dq = deque(tasks)
cnt = 0
ans = 1
for i in range(1,len(tasks)):
    if tasks[i-1] == tasks[i] and cnt <= 3:
        dq.popleft()
    else:
       ans += 1
       cnt = 0
       back = dq[0]
       dq.popleft()
       dq.append(back)
if len(dq) < len(set_tasks):
    print(-1)
else:
    print(ans)
